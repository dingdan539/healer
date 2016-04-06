报警接入
-------------

.. http:post:: http://oms.yihaodian.com.cn/healer/api/alert

   参数：

   :param ip: alarm's ip
   :param pool_id: auto search by ip if null
   :type pool_id: int
   :param site_id: auto search by ip if null
   :type site_id: int
   :param description: 报警内容
   :type description: json
   :param level_id: 3-中间件层 4-应用层 5-业务层
   :type level_id: int
   :param source_id: 1-zabbix 2-healthcheck ...
   :type source_id: int

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
          "code": 1,
          "title": "succ",
          "description": "success"
      }

      or

      HTTP/1.1 400 OK
      Content-Type: application/json

      {
          "code": 0,
          "title": "error",
          "description": "token is not found"
      }
