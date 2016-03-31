报警屏蔽
-------------

.. http:post:: http://oms.yihaodian.com.cn/healer/api/shield

   可选择以下参数来设置屏蔽策略，条件组合“与”：

   :param ip: alarm's ip
   :param pool_id: auto search by ip if null
   :type pool_id: int
   :param site_id: auto search by ip if null
   :type site_id: int
   :param source_id: 1-zabbix 2-healthcheck ...
   :type source_id: int
   :param key: description keyword
   :type key: string
   :param start_time: shiled start time eg:2015-12-23 23:11:01
   :type key: string
   :param duration: 从start_time 开始持续多久（秒）。默认3600秒（1小时）
   :type duration: int

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
