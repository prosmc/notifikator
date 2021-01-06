
Changes
=========

0.2.0 (2021-01-06)
---------------------
* Added - Sync adapter functinality  was activated in 'handler.py'.
* Added - Templates for 'query-03' were added which is important for the sync simulator adapter.
* Added - Three new jinja templated files were initially added.
* Added - The 'scripts-02.json.j2' template file was initially committed.
* Added - The following files were added or modified due to code optimizations (refactoring).
* Added - Integration of different types of processors which can be parameterized.
* Added - 'state' parameter was added to the 'query-01.json.j2' template.
* Added - The parameter 'state' was added to the 'get_search_query_result' method of 'query.py'.
* Added - Parameter 'state' was added to the 'execute' method of 'processor.py'.
* Fixed - The '__str__' method was changed in 'simulator.py' due to a wrong string definition.
* Updated - Release '0.2.0' wad defined in the following three files '.xrc', '.env' and 'setup.py'.
* Updated - The 'PubSimulatorAdapter' was renamed into 'PubDemoAdapter' and the 'SyncSimulatorAdapter' was renamed into 'SyncDemoAdapter'.
* Updated - 'script-02.json.j2' was modified for working with the synchronizer processor.
* Updated - 'app/bootstrap.py' was refactore for working with publisher and synchronizer processes.
* Updated - 'Sync Simulator Adapter' was improved for the first working revision.
* Updated - All 'subscriber' artifacts  were replaced by 'synchronizer' artifacts.
* Updated - Due to a config improvement in 'app/__init__.py' the 'bootstrap.py' and 'processor.py' were modified.
* Updated - Config definition in '__init__.py' was improved.
* Updated - Some template files were renamed.

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
