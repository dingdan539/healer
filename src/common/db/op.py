# -*- coding:utf-8 -*-
from ...function.decorator import *
from father import *
from ...function import basic as fb
from ...config.db.databases import dbmaps
from ...config import load_config_auto
from sqlalchemy import Table, text, or_
from ...config.db import models


@singleton
class DbOp(object):
    __instance = None

    def __init__(self, tag, **kwargs):
        self.__instance = DbSqlalchemy(**kwargs)

    def get_engine(self):
        return self.__instance.engine

    def get_session(self):
        return self.__instance.session


class InitCreateDb(object):
    def __init__(self, db_name):
        self.prefix = dbmaps[db_name]['prefix']
        self.tables = dbmaps[db_name]['tables']
        cfg = load_config_auto()
        self.dbargs = fb.get_profix_property(cfg, self.prefix)
        self.dbargs['DEBUG'] = cfg.DEBUG
        self.dbargs['PREFIX'] = self.prefix
        self.dbargs['DB_NAME'] = db_name


class CreateDb(InitCreateDb):
    __db_name = None
    __instance = None
    __engine = None
    __session = None

    error_map = {
        0: 'succ',
        1: 'db is empty in config',
        2: 'field must not empty'
    }

    @staticmethod
    def __default_args(**kwargs):
        params = dict()
        params['tb_name'] = kwargs.get('tb_name', '')
        params['field'] = kwargs.get('field', [])
        params['where'] = kwargs.get('where', {})
        params['or'] = kwargs.get('or', {})
        params['in'] = kwargs.get('in', {})
        params['order'] = kwargs.get('order', {})
        params['limit'] = kwargs.get('limit', [])
        return params

    @staticmethod
    def __get_columns(cs):
        data = []
        for i in cs:
            data.append(i.__dict__)
        return data

    def __init__(self, db_name):
        super(CreateDb, self).__init__(db_name)
        self.__db_name = db_name
        self.__instance = DbOp(db_name, **self.dbargs)
        self.__engine = self.__instance.get_engine()
        self.__session = self.__instance.get_session()
        if models.DeferredReflection in getattr(models, self.__db_name.capitalize()).__bases__:
            getattr(models, self.__db_name.capitalize()).prepare(self.__engine)

    def init_table(self):
        tbs = []
        for i in self.tables:
            tbs.append(getattr(getattr(models, i.capitalize()), '__table__'))
        getattr(models, self.__db_name.capitalize()).metadata.create_all(bind=self.__engine, tables=tbs)

    def execute(self, sql):
        try:
            my_prefix = sql[:sql.index(' ')].lower()
            res = self.__session.execute(sql)
            if my_prefix == 'select':
                k = res.keys()
                data = res.fetchall()
                return [dict(zip(k, i)) for i in data]

            elif my_prefix in ['update', 'delete']:
                return res.rowcount
            elif my_prefix == 'insert':
                return res.lastrowid
            else:
                return False
        except Exception, data:
            print data

    def __output(self, code, data=[]):
        return {'code': code, 'msg': self.error_map[code], 'data': data}

    def search(self, **kwargs):
        """
        Args:
            tb_name - str
            field   - [] - ['name', 'tag', 'datatime'] 选取的字段
            where   - {} - {'id >=': 55}
            or      - {} - {'id >=': 55, 'name like': '%x%'}
            in      - {} - {'id': [1, 2, 5, 66]}
            order   - {} - {'name': 'desc'}
            limit   - [] - [5] or [1, 5]  单个表示limit(5) 2个表示limit(5).offset(1)
        Returns:
            {'msg': 'succ', 'code': 0, 'data': []} data 是数据
        """
        params = self.__default_args(**kwargs)
        tb_name = params['tb_name']
        if tb_name not in dbmaps[self.__db_name]['tables']:
            return self.__output(1)

        # users_table = Table(tb_name, Base.metadata, autoload_with=self.__engine)
        # column_dicts = [i.name for i in users_table.columns]

        # 动态加载表结构
        t = getattr(models, tb_name.capitalize())

        # field过滤
        p_f = params['field']
        field = [t] if len(p_f) == 0 else [getattr(t, i) for i in p_f]
        result = self.__session.query(*field)

        # where过滤
        p_w = params['where']
        if p_w:
            for key in p_w:
                cc, k = key.split(' ')
                if k in ['>', '>=', '<', '<=', '=', '!=']:
                    result = result.filter(text(''.join([key, "'", str(p_w[key]), "'"])))
                elif k == 'like':
                    result = result.filter(getattr(getattr(t, cc), k)(p_w[key]))

        # or过滤
        p_o = params['or']
        if p_o:
            pas = []
            for key in p_o:
                cc, k = key.split(' ')
                if k in ['>', '>=', '<', '<=', '=', '!=']:
                    pas.append(text(''.join([key, "'", str(p_o[key]), "'"])))

                elif k == 'like':
                    pas.append(getattr(getattr(t, cc), k)(p_o[key]))

            result = result.filter(or_(*pas))

        # in过滤
        p_i = params['in']
        if p_i:
            for cc in p_i:
                result = result.filter(getattr(getattr(t, cc), 'in_')(p_i[cc]))

        # order过滤
        p_order = params['order']
        if p_order:
            for key in p_order:
                result = result.order_by(text(key+' '+str(p_order[key])))

        # limit过滤
        p_l = params['limit']
        if len(p_l) == 1:
            result = result.limit(p_l[0])
        elif len(p_l) == 2:
            result = result.limit(p_l[1]).offset(p_l[0])

        res = result.all()

        # 返回处理好的数据
        data = []
        if len(p_f) == 0:
            data = self.__get_columns(res)
        else:
            for dd in res:
                tmp = {}
                for i, value in enumerate(dd):
                    tmp[p_f[i]] = value
                data.append(tmp)
        return self.__output(0, data)

    def update(self, **kwargs):
        """
        Args:
            tb_name - str
            field   - {} - {'name': 'dd'}
            where   - {} - {'id >=': 55}

        Returns:
            {'msg': 'succ', 'code': 0, 'data': 3} data 是更新的条数
        """
        p_f = kwargs.get('field', {})
        p_w = kwargs.get('where', {})

        tb_name = kwargs.get('tb_name', '')
        if tb_name not in dbmaps[self.__db_name]['tables']:
            return self.__output(1)

        # 动态加载表结构
        t = getattr(models, tb_name.capitalize())
        result = self.__session.query(t)

        if p_w:
            for key in p_w:
                cc, k = key.split(' ')
                if k in ['>', '>=', '<', '<=', '=', '!=']:
                    result = result.filter(text(''.join([key, "'", str(p_w[key]), "'"])))
                elif k == 'like':
                    result = result.filter(getattr(getattr(t, cc), k)(p_w[key]))

        result = result.update(p_f, synchronize_session=False)

        return self.__output(0, data=result)

    def insert(self, **kwargs):
        """
        Args:
            field - {} or [{},{}] | {'name': 'dd'} or [{'name': 'dd'}, {'name': 'dd2', 'tag': 'tom'}]

        Returns:
            <src.config.db.models.Alert_2016 object at 0x00000000044E8B70>
            {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000000004444BA8>, u'description':
             '10.4.29.175OK:...    ', u'type_id': 15L, u'ip': '10.4.29.175', u'level_id': 3L}
            or
            [<src.config.db.models.Alert_2016 object at 0x00000000044E8B70>, ...]
        """
        p_f = kwargs.get('field', {})

        tb_name = kwargs.get('tb_name', '')
        if tb_name not in dbmaps[self.__db_name]['tables']:
            return self.__output(1)

        # 动态加载表结构
        t = getattr(models, tb_name.capitalize())

        with self.__session.begin():
            if isinstance(p_f, dict):
                tb_ins = t(**p_f)
                self.__session.add(tb_ins)
                self.__session.flush()
                return tb_ins
            elif isinstance(p_f, list):
                lists = []
                for i in p_f:
                    lists.append(t(**i))
                self.__session.add_all(lists)
                self.__session.flush()
                return lists


    def delete(self, **kwargs):
        """
        Args:
            tb_name - str
            where   - {} - {'id >=': 55}

        Returns:
            {'msg': 'succ', 'code': 0, 'data': 3} data 是删除的条数
        """
        p_w = kwargs.get('where', {})

        tb_name = kwargs.get('tb_name', '')
        if tb_name not in dbmaps[self.__db_name]['tables']:
            return self.__output(1)

        # 动态加载表结构
        t = getattr(models, tb_name.capitalize())
        result = self.__session.query(t)

        if p_w:
            for key in p_w:
                cc, k = key.split(' ')
                if k in ['>', '>=', '<', '<=', '=', '!=']:
                    result = result.filter(text(''.join([key, "'", str(p_w[key]), "'"])))
                elif k == 'like':
                    result = result.filter(getattr(getattr(t, cc), k)(p_w[key]))

        result = result.delete(synchronize_session=False)

        return self.__output(0, data=result)