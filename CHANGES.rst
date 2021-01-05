
Changes
=========

0.1.3 (2021-01-05)
---------------------
* Added - Params 'APP_PUBLISHER_SLEEP_TIME' and 'APP_SUBSCRIBER_SLEEP_TIME' were added to the following files ...
* Added - Two different Pub/Sub Threads were defined.
* Added - Log-Messages are added to the pub/sub adapters.
* Fixed - Wrong release definition was fixed in '.env'.
* Updated - Legend was renamed into 'REP-Stack'.
* Updated - The name for the Dashboard was changed into '[REP-STACK]'.
* Updated - Release '0.1.2' was defined in the following files.
* Updated - Code beautifying.
* Updated - Function 'send' was renamed into 'publish' and function 'request' was renamed into 'subscribe'.
* Updated - Short hand function 'x_setup_eps' was renamed into 'x_setup_rep_stack'.

0.1.2 (2021-01-03)
---------------------
* Added   - Initial commit of the class 'SimulatorAdapter' of type subscriber.
* Added   - Initial commit of the class 'QueryHandler'.
* Added   -  Enum 'ProcessorUnitType' was added and the class 'Processor' was extended by the 'unit_type' property.
* Updated - Both template files were improved.
* Updated - Function 'get_search_query_result' was moved from the class 'Processor' to the class 'QueryHandler'.
* Updated - app.config['APP_INDEX_FILTER_QUERY'] was modified.
* Updated - Function 'x_setup_kl_stack' was renamed into 'x_setup_esp'.
* Updated - Title was changed from '[EPF] IMTickets/Incidents' to '[EPS] IMTickets/Incidents'.
* Updated - Implementation of the 'adatper' pattern for the modularization of the publisher/subscriber plugin capability.
* Updated - Dashboard/Visualization for the notifikator services was updated.
* Updated - 'processor.py' was optimized for the implementation of the 'adapter' pattern.
* Updated - 'bootstrap.py' was optimized for the implementation of the 'adapter' pattern.
* Updated - 'bootstrap.py' was modified due to the extension of the 'Processor' class.
* Updated - 'simulator.py' was moved to the 'app/adapters/sender/' folder.
* Updated - Class 'Adapter' was removed from '__init__.py' and moved to separate file.

0.1.1 (2020-12-30)
---------------------
* Added   - 'simulator.py' is initially committed as replacement for 'elasticsearch.py'.
* Added   -  Function 'notify' was renamed into 'execute' in 'processor.py'. - Function class 'Adapter' was refactored in '__init__.py'.
* Added   - Function 'get_search_query_result' was implemented.
* Added   - Initial commit of the Adapter class stub.
* Added   - First simple implementation of the 'ElasticsearchAdapter'.
* Added   - Initial version of the 'Elasticsearch' Adapter was added.
* Fixed   - Formatting error in 'query_01.json.j2' was fixed.
* Fixed   - Some wrong defined environment variables were fixed.
* Updated - 'Elasticsearch.py' was replaced by 'Simulator.py'.
* Updated - function 'create_dashboard' was modified for importing 'saved objects' by overwriting them.
* Updated - Default value for config parameter 'APP_ID' was set to 'nk01'.
* Updated - function 'create_index_pattern()' was deactivated and in return function 'create_dashboards()' was activated.
* Updated - 'notifikator_01.ndjson.j2' was replaced by 'notifikator.ndjson.j2'.
* Updated - Some logging info messages were adapted.
* Updated - Class Adatpter was refactored.
* Updated - Comment was added to 'bootstrap.py'.
* Updated - .gitattributes were modified.

0.1.0 (2020-12-23)
---------------------
* Added   - Initial commit of all 'notifikator' project files.
