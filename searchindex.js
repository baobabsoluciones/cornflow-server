Search.setIndex({docnames:["clients/admin-spa","clients/index","clients/python-api","deploy/access","deploy/docker-compose.yml","deploy/docker-stack","deploy/index","deploy/intro","deploy/logs","deploy/options","deploy/problems","deploy/production","deploy/simultaneous","dev/cornflow_client","dev/endpoints","dev/index","dev/models","examples/graph_coloring","examples/index","examples/scheduling","examples/vrp","guides/debug_with_airflow","guides/deploy_solver","guides/deploy_solver_new","guides/index","guides/jsonschema","guides/testing_app","guides/use_solver","index","main/architecture","main/concepts","main/examples","main/index","main/install","main/introduction","stable-rest-api-ref"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.todo":2,sphinx:56},filenames:["clients/admin-spa.rst","clients/index.rst","clients/python-api.rst","deploy/access.rst","deploy/docker-compose.yml.rst","deploy/docker-stack.rst","deploy/index.rst","deploy/intro.rst","deploy/logs.rst","deploy/options.rst","deploy/problems.rst","deploy/production.rst","deploy/simultaneous.rst","dev/cornflow_client.rst","dev/endpoints.rst","dev/index.rst","dev/models.rst","examples/graph_coloring.rst","examples/index.rst","examples/scheduling.rst","examples/vrp.rst","guides/debug_with_airflow.rst","guides/deploy_solver.rst","guides/deploy_solver_new.rst","guides/index.rst","guides/jsonschema.rst","guides/testing_app.rst","guides/use_solver.rst","index.rst","main/architecture.rst","main/concepts.rst","main/examples.rst","main/index.rst","main/install.rst","main/introduction.rst","stable-rest-api-ref.rst"],objects:{"cornflow.endpoints":{dag:[14,0,0,"-"],execution:[14,0,0,"-"],instance:[14,0,0,"-"],login:[14,0,0,"-"],signup:[14,0,0,"-"],user:[14,0,0,"-"]},"cornflow.endpoints.dag":{DAGEndpoint:[14,1,1,""],DAGEndpointManual:[14,1,1,""]},"cornflow.endpoints.dag.DAGEndpoint":{ROLES_WITH_ACCESS:[14,2,1,""],get:[14,3,1,""],methods:[14,2,1,""],put:[14,3,1,""]},"cornflow.endpoints.dag.DAGEndpointManual":{ROLES_WITH_ACCESS:[14,2,1,""],methods:[14,2,1,""],post:[14,3,1,""]},"cornflow.endpoints.execution":{ExecutionDataEndpoint:[14,1,1,""],ExecutionDetailsEndpoint:[14,1,1,""],ExecutionDetailsEndpointBase:[14,1,1,""],ExecutionEndpoint:[14,1,1,""],ExecutionLogEndpoint:[14,1,1,""],ExecutionStatusEndpoint:[14,1,1,""]},"cornflow.endpoints.execution.ExecutionDataEndpoint":{get:[14,3,1,""],methods:[14,2,1,""]},"cornflow.endpoints.execution.ExecutionDetailsEndpoint":{"delete":[14,3,1,""],get:[14,3,1,""],methods:[14,2,1,""],post:[14,3,1,""],put:[14,3,1,""]},"cornflow.endpoints.execution.ExecutionEndpoint":{get:[14,3,1,""],methods:[14,2,1,""],post:[14,3,1,""]},"cornflow.endpoints.execution.ExecutionLogEndpoint":{get:[14,3,1,""],methods:[14,2,1,""]},"cornflow.endpoints.execution.ExecutionStatusEndpoint":{get:[14,3,1,""],methods:[14,2,1,""]},"cornflow.endpoints.instance":{InstanceDataEndpoint:[14,1,1,""],InstanceDetailsEndpoint:[14,1,1,""],InstanceDetailsEndpointBase:[14,1,1,""],InstanceEndpoint:[14,1,1,""],InstanceFileEndpoint:[14,1,1,""],allowed_file:[14,4,1,""]},"cornflow.endpoints.instance.InstanceDataEndpoint":{get:[14,3,1,""],methods:[14,2,1,""]},"cornflow.endpoints.instance.InstanceDetailsEndpoint":{"delete":[14,3,1,""],methods:[14,2,1,""],put:[14,3,1,""]},"cornflow.endpoints.instance.InstanceDetailsEndpointBase":{get:[14,3,1,""],methods:[14,2,1,""]},"cornflow.endpoints.instance.InstanceEndpoint":{get:[14,3,1,""],methods:[14,2,1,""],post:[14,3,1,""]},"cornflow.endpoints.instance.InstanceFileEndpoint":{methods:[14,2,1,""],post:[14,3,1,""]},"cornflow.endpoints.login":{LoginEndpoint:[14,1,1,""]},"cornflow.endpoints.login.LoginEndpoint":{auth_db_authenticate:[14,3,1,""],auth_ldap_authenticate:[14,3,1,""],methods:[14,2,1,""],post:[14,3,1,""]},"cornflow.endpoints.signup":{SignUpEndpoint:[14,1,1,""]},"cornflow.endpoints.signup.SignUpEndpoint":{methods:[14,2,1,""],post:[14,3,1,""]},"cornflow.endpoints.user":{ToggleUserAdmin:[14,1,1,""],UserDetailsEndpoint:[14,1,1,""],UserEndpoint:[14,1,1,""]},"cornflow.endpoints.user.ToggleUserAdmin":{ROLES_WITH_ACCESS:[14,2,1,""],methods:[14,2,1,""],put:[14,3,1,""]},"cornflow.endpoints.user.UserDetailsEndpoint":{"delete":[14,3,1,""],get:[14,3,1,""],methods:[14,2,1,""],put:[14,3,1,""]},"cornflow.endpoints.user.UserEndpoint":{ROLES_WITH_ACCESS:[14,2,1,""],get:[14,3,1,""],methods:[14,2,1,""]},"cornflow.models":{execution:[16,0,0,"-"],instance:[16,0,0,"-"],user:[16,0,0,"-"]},"cornflow.models.execution":{ExecutionModel:[16,1,1,""]},"cornflow.models.execution.ExecutionModel":{update_state:[16,3,1,""]},"cornflow.models.instance":{InstanceModel:[16,1,1,""]},"cornflow.models.user":{UserModel:[16,1,1,""]},"cornflow.models.user.UserModel":{"delete":[16,3,1,""],check_email_in_use:[16,3,1,""],check_hash:[16,3,1,""],check_username_in_use:[16,3,1,""],disable:[16,3,1,""],get_all_users:[16,3,1,""],get_one_user:[16,3,1,""],get_one_user_by_email:[16,3,1,""],get_one_user_by_username:[16,3,1,""],update:[16,3,1,""]},"cornflow_client.constants":{AirflowError:[13,5,1,""],InvalidUsage:[13,5,1,""]},"cornflow_client.constants.AirflowError":{args:[13,2,1,""],error:[13,2,1,""],status_code:[13,2,1,""],to_dict:[13,3,1,""],with_traceback:[13,3,1,""]},"cornflow_client.constants.InvalidUsage":{args:[13,2,1,""],error:[13,2,1,""],status_code:[13,2,1,""],to_dict:[13,3,1,""],with_traceback:[13,3,1,""]},"cornflow_client.core":{application:[13,0,0,"-"],experiment:[13,0,0,"-"],instance:[13,0,0,"-"],instance_solution:[13,0,0,"-"],solution:[13,0,0,"-"]},"cornflow_client.core.application":{ApplicationCore:[13,1,1,""],NoSolverException:[13,5,1,""]},"cornflow_client.core.application.ApplicationCore":{get_default_solver_name:[13,3,1,""],get_schemas:[13,3,1,""],get_solver:[13,3,1,""],instance:[13,3,1,""],name:[13,3,1,""],schema:[13,3,1,""],solution:[13,3,1,""],solve:[13,3,1,""],solvers:[13,3,1,""],test_cases:[13,3,1,""]},"cornflow_client.core.experiment":{ExperimentCore:[13,1,1,""]},"cornflow_client.core.experiment.ExperimentCore":{check_solution:[13,3,1,""],get_objective:[13,3,1,""],instance:[13,3,1,""],solution:[13,3,1,""],solve:[13,3,1,""]},"cornflow_client.core.instance":{InstanceCore:[13,1,1,""]},"cornflow_client.core.instance_solution":{InstanceSolutionCore:[13,1,1,""]},"cornflow_client.core.instance_solution.InstanceSolutionCore":{check_schema:[13,3,1,""],data:[13,3,1,""],from_dict:[13,3,1,""],from_json:[13,3,1,""],generate_schema:[13,3,1,""],schema:[13,3,1,""],to_dict:[13,3,1,""],to_json:[13,3,1,""]},"cornflow_client.core.solution":{SolutionCore:[13,1,1,""]},"cornflow_client.cornflow_client":{CornFlow:[13,1,1,""],CornFlowApiError:[13,5,1,""]},"cornflow_client.cornflow_client.CornFlow":{api_for_id:[13,3,1,""],create_case:[13,3,1,""],create_execution:[13,3,1,""],create_instance:[13,3,1,""],create_instance_file:[13,3,1,""],delete_api_for_id:[13,3,1,""],delete_one_case:[13,3,1,""],delete_one_instance:[13,3,1,""],get_all_cases:[13,3,1,""],get_all_executions:[13,3,1,""],get_all_instances:[13,3,1,""],get_all_users:[13,3,1,""],get_api_for_id:[13,3,1,""],get_data:[13,3,1,""],get_log:[13,3,1,""],get_one_case:[13,3,1,""],get_one_instance:[13,3,1,""],get_one_user:[13,3,1,""],get_results:[13,3,1,""],get_schema:[13,3,1,""],get_solution:[13,3,1,""],get_status:[13,3,1,""],is_alive:[13,3,1,""],login:[13,3,1,""],manual_execution:[13,3,1,""],patch_api_for_id:[13,3,1,""],patch_one_case:[13,3,1,""],post_api_for_id:[13,3,1,""],put_api_for_id:[13,3,1,""],put_one_case:[13,3,1,""],sign_up:[13,3,1,""],stop_execution:[13,3,1,""],write_solution:[13,3,1,""]},"cornflow_client.cornflow_client.cornflow_client.constants":{SOLUTION_STATUS_FEASIBLE:[13,6,1,""],SOLUTION_STATUS_INFEASIBLE:[13,6,1,""],STATUS_INFEASIBLE:[13,6,1,""],STATUS_MEMORY_LIMIT:[13,6,1,""],STATUS_NODE_LIMIT:[13,6,1,""],STATUS_NOT_SOLVED:[13,6,1,""],STATUS_OPTIMAL:[13,6,1,""],STATUS_TIME_LIMIT:[13,6,1,""],STATUS_UNBOUNDED:[13,6,1,""],STATUS_UNDEFINED:[13,6,1,""]},cornflow_client:{constants:[13,0,0,"-"],cornflow_client:[13,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","attribute","Python attribute"],"3":["py","method","Python method"],"4":["py","function","Python function"],"5":["py","exception","Python exception"],"6":["py","data","Python data"]},objtypes:{"0":"py:module","1":"py:class","2":"py:attribute","3":"py:method","4":"py:function","5":"py:exception","6":"py:data"},terms:{"0cfdd4debaab":4,"104":8,"10863a20e7d6":4,"1168103":8,"118":8,"1185":8,"1246":8,"129fd9b29361":12,"1370681":8,"1377544":8,"1454702":8,"146":8,"149":8,"1495255":8,"173":8,"200":8,"201":14,"2021":8,"20210518t173709":8,"20210519t173726":8,"20210519t173728":8,"2037":3,"2037bi":3,"20m":8,"251":8,"2d5200460cfb":12,"400":[11,13],"403":11,"443":11,"4c872f5b6647":12,"500":11,"5000":[4,9,11,12,33],"5432":[4,11,12],"5555":[4,12],"571":8,"588":8,"5a96cc04b69b":12,"629":8,"636":3,"6379":12,"654":8,"65de0e382a04":12,"68d8f7db53ac":12,"7a7b10d09a46":12,"7d6e114978af":12,"8080":[4,9,12,33],"8389735999d5":12,"8793":[4,12],"9bc91747cd37":4,"abstract":[13,29,30],"break":11,"case":[12,13,21,24,30],"class":[3,14,15,16,24,26],"default":[5,6,8,10,11,13,17,18,19,23,25,26,33],"enum":25,"export":[13,33],"final":[5,23,34],"float":[13,23,25],"function":[0,8,11,13,22,26,30],"import":[3,23,25,26,27,35],"int":[14,16],"long":[30,34],"new":[0,3,5,12,13,14,16,24,25,28,29,34],"public":[18,19,26],"return":[3,8,11,13,14,16,22,23,26,29,30,34],"static":[14,16],"super":[3,26],"true":[9,13],"try":[10,21,28],"var":5,"while":[17,20,27],Being:34,But:[14,34],For:[3,5,9,12,25,31,33,34],KMS:11,Not:[3,10],One:[10,30],TLS:3,That:5,The:[0,2,3,5,6,8,10,12,13,16,17,18,19,20,23,24,25,26,29,30,31,33,34,35],Then:[9,25],There:[5,19,20,22,23,28,29],These:[5,12,14,23,26],Use:[24,28],Will:26,With:[6,11],__file__:23,__init__:[8,24,26],__pycache__:8,__traceback__:13,_class:16,a7f2868e9329:12,abc:13,abl:30,about:[8,9,11,33],accept:[14,25,30,34],access:[6,8,9,10,11,13,14,22,27,28],access_init:[10,33],accord:13,account:[3,12,20],action:[3,13],activ:[3,8,11,33],actual:[16,30],add:[22,25,26],addit:[3,12,26],address:[3,9,10],adequ:11,admin:[3,5,10,11,14,21,33],administ:0,administr:[3,5,11],adminnistrator1234:11,advantag:34,advis:3,affect:3,after:[5,8,16,19],afvenv:33,again:[3,10,34],against:[3,8],agil:6,agnost:34,ago:[4,12],aiflow:12,airflow:[4,6,12,14,16,21,32],airflow__api__auth_backend:33,airflow__celery__broker_url:12,airflow__celery__flower_url_prefix:9,airflow__core__dags_are_paused_at_cr:33,airflow__core__load_exampl:33,airflow__webserver__base_url:9,airflow__webserver__enable_proxy_fix:9,airflow__webserver__secret_kei:33,airflow_config:[4,5,10,33],airflow_conn_cf_uri:[3,9,33],airflow_db:5,airflow_db_host:5,airflow_db_password:5,airflow_db_port:5,airflow_db_us:5,airflow_hom:[8,33],airflow_pwd:[3,5,9,10,33],airflow_statu:8,airflow_test:33,airflow_test_password:33,airflow_url:[5,9,33],airflow_us:[3,5,9,10,33],airflow_vers:33,airflowerror:13,algorithm1:[20,26,27],algorithm2:20,algorithm3:20,algorithm:30,aliv:13,all:[3,4,7,8,9,10,11,12,13,14,16,19,22,23,25,26,30,31,33],allow:[0,3,5,6,12,34],allowed_fil:14,allowedtrail:25,along:26,alreadi:[14,33,34],also:[0,3,5,11,12,18,22,23,25,26,29,30,33,34],altern:25,alwai:[3,25],amazon:9,amd64:10,among:30,ancestor:[8,33],ani:[0,3,6,9,10,18,21,29,30,31,34],anoth:[3,19,26,30],answer:30,apach:[29,33],api:[0,1,3,8,13,14,28,29,31,33],api_for_id:13,app:[0,5,8,22,23,26,27,29,31,33],appbuild:3,appli:13,applic:[3,5,6,8,11,13,21,24,25,26,31,34],applicationcor:[15,23],appropri:31,apt:10,arbitrari:23,arc:[17,23,25],architectur:[12,28,32],arg:[13,23],argument:[10,12,13,18,21,22],arrai:25,articl:30,ask:[13,18,29],assign:[3,17,29],assum:[25,33],attach:5,attent:3,attribut:[3,25],auditori:3,auth:[6,33],auth_db:3,auth_db_authent:14,auth_ldap:3,auth_ldap_authent:14,auth_typ:3,authent:[6,14],automat:16,aux:33,auxiliari:25,avail:[4,12,17,18,19,20,23,34],awk:33,back:[14,16],backend:[3,6,33],bad:[10,11,23],balanc:9,baobabsolucion:[0,4,5,8,9,12,19,27,33],base:[3,13,14,16,33,34],basedagtest:26,basedatamodel:16,bash:[8,10,33],basic:[0,11,12,24],basic_auth:33,becaus:[8,10,23,25],becom:34,befor:[3,4,6,9,11,25,28],begin:[6,28],being:[3,34],benchmark:8,besid:23,best:[6,25,30],better:[23,30],between:[3,16,19,25,29,30],big:30,bin:33,bind:3,bit:8,bodi:14,bool:16,both:[8,22,30],branch:5,broker:[11,12],brows:28,browser:10,build:[6,29,32],built:[0,5,11,17,19,20,22,29,31,34],buster:5,c477c235b199:4,c56e3444078c:12,c5d3fdad4c6b:12,calcul:30,call:[8,9,21,25,29,30],can:[0,2,3,4,5,6,8,10,11,12,14,18,21,22,23,25,26,27,30,32,33],cannot:3,capabl:29,capac:20,capacit:20,care:[17,30],carri:3,catalogu:23,cbc:19,celeri:[11,12,33],celeryexecutor:[5,12,33],cell:25,center:34,certain:[5,14,16,23,30],certif:11,cfg:9,cfvenv:33,chang:[3,5,9,11,14],characterist:[3,22,30],charg:31,check:[2,3,4,5,7,8,10,13,14,16,18,21,23,26,34],check_email_in_us:16,check_hash:16,check_schema:13,check_solut:[13,23],check_username_in_us:16,choos:20,classmethod:13,clean:[6,16,33],clean_historic_data:10,clear:30,client:[2,15,24,28,31,32],clone:[10,33],close:20,closest:20,cloud:9,code:[3,6,8,10,11,13,14,16,24,26,28,29,33,34],collect:34,color:[18,28,31],column:25,com:[3,4,9,11,12,19,33],come:22,command:[4,5,8,12,16,31],comment:25,commerci:29,common:[3,13,24],commun:[0,3,7,11,12,14],compar:[3,30],compat:10,complement:25,complet:[24,30,33,34],complex:30,compli:[13,34],complic:8,compon:32,compos:[5,6,7,9,10,11,12,28,33],compress:8,comput:[4,30],conceiv:33,concept:[22,28,29,32],condit:[4,10],conf:[11,35],config:[10,11,13,16,22,23,29,33],configschema:[14,16],configur:[3,7,8,9,11,13,16,18,22,23,24,29,32],confirm:[3,14],connect:[3,5,6,11,29],consist:[17,20,23,30,33],consol:8,constant:15,constitut:[3,22],constraint:[25,33],constraint_url:33,constructor:13,consult:3,consum:[12,19],contain:[4,5,6,7,8,10,12,16,22,23,25,33],content:[1,3,6,13,15,24,32,35],context:10,continu:[3,6],contrari:34,control:[6,28],conveni:[11,30],convert:25,cooki:10,coordin:25,core:[15,23],corn:[4,9,10,12,33],corn_airflow_db_1:[4,12],corn_cornflow_1:[4,12],corn_cornflow_db_1:[4,12],corn_flower_1:12,corn_redis_1:12,corn_scheduler_1:12,corn_webserver_1:[4,12],corn_worker_1:12,corn_worker_2:12,corn_worker_3:12,cornflow1234:11,cornflow:[0,2,5,11,12,14,15,16,18,22,24,26,27,30,31,32,34],cornflow_admin:[3,33],cornflow_admin_email:3,cornflow_admin_password:33,cornflow_admin_pwd:[3,5],cornflow_admin_us:[3,5],cornflow_cli:[13,18,23,27,33],cornflow_db_conn:5,cornflow_db_host:10,cornflow_log:8,cornflow_service_mail:3,cornflow_service_pwd:[3,5],cornflow_service_us:[3,5],cornflow_statu:8,cornflow_url:5,cornflowadmin1234:3,cornflowapierror:13,cornflowdb:9,cornflowrol:11,cornflowserveraddress:3,cornflowserverport:3,correctli:11,correspond:[23,26],could:[9,10,12,22,25,34],cover:10,cplex:[29,31],cpo:31,creat:[3,4,5,8,9,10,11,12,13,14,16,22,23,29,33],create_admin_us:[10,33],create_cas:13,create_execut:[13,27],create_inst:[13,27],create_instance_fil:13,create_service_us:[10,33],created_at:16,creation:[0,3,16],credenti:3,crt:11,csrf:10,curl:[4,9,12],current:[13,18,20,29,34],custom:[5,20,25],cut:33,cvrp:20,cycl:5,d2730ce4b8c1:12,dag:[3,4,5,8,11,15,17,18,19,20,21,22,23,26,27,29,33],dag_id:8,dag_nam:13,dag_tim:8,dagendpoint:14,dagendpointmanu:14,dagrun:29,daili:8,data:[5,6,11,13,14,16,21,22,23,25,26,27,30,32,34],data_hash:16,databas:[3,4,5,6,16,32],database_url:[9,11,33],dataschema:[14,16],dataset:[13,23,31],datat:3,date:[2,3,8,16,21],datetim:16,debug:[24,28],decid:[19,23,30],decis:32,decrypt:12,def:[23,26],defin:[3,5,10,12,13,22,23,25,26,34],definit:6,deleg:3,delet:[0,3,10,13,14,16],delete_api_for_id:13,delete_one_cas:13,delete_one_inst:13,deleted_at:16,deliv:20,demand:25,demo:34,demonstr:12,deni:10,depend:[7,8,12,16,22,25,30,33],deploi:[4,8,9,10,11,12,24,28,33,34],deploy:[3,5,6,8,10,12,23,28,33,34],deprec:3,describ:[6,25,30,34],descript:[13,14,16,25],design:30,desktop:31,destroi:8,determin:30,determinist:25,dev:[10,33],develop:[3,5,6,23,33],devsm:[0,27],dict:[13,14,16,23,26,27],dictionari:[13,14,22,23,25],differ:[3,5,6,8,12,14,17,30],differenti:3,difficult:10,dir:8,directli:8,directori:[3,4,5,8,13,23],dirnam:23,disabl:16,displai:[5,25],distanc:20,divid:[8,30],divis:30,doc:[3,8],docker:[6,7,8,9,11,12,28,32],dockerfil:[5,10],document:[2,3,8,9,10,11,23,33],doe:[3,8,9,10,11,14,16,19,20,21,29,30],doing:3,domain:3,don:[10,33],done:[3,8,22],doubl:7,down:[4,12,33],download:[13,18,33],downstream:8,drive:12,dumb:20,durat:19,dure:[14,16],e13c87bcd36b:12,e98dfc643ddd:12,e9adafa751fd35adfc1fdd3285019be15eea0758f76e38e1e37a1154fb36:33,each:[3,12,13,19,20,22,23,25,26,30,33],easi:29,easiest:[3,34],ec86c6761b80:12,edg:17,edit:[0,7,13,14],editor:22,either:[14,30],elb:9,element:13,email:[3,13,16,33],enabl:11,encrypt:[3,5,9,11,12],end:23,end_dat:8,endpoint:[3,8,15,16,28],enforc:6,engin:[5,8,9,33],enough:[22,30],entir:9,entiti:14,entri:[3,10],entrypoint:[4,6,10,12],env:9,environ:[3,6,8,9,10,11,12,33],error:[8,10,11,13,14,16,24,26],error_pag:11,essenti:6,etc:[11,16,23,25,29,31],even:[8,16,21,25],evenli:30,event:3,everi:[5,8],everyth:23,exact:30,exactli:22,exampl:[0,3,9,11,12,21,23,24,28,30,33,34],exc:10,except:[13,23,24],exec:[8,33],execut:[0,3,5,8,9,10,12,13,15,18,19,21,22,27,29,32,33],execution_config:27,execution_d:8,execution_id:[13,27],executiondataendpoint:14,executiondetailsendpoint:14,executiondetailsendpointbas:14,executionendpoint:14,executionlogendpoint:14,executionmodel:16,executionstatusendpoint:14,executor:[5,12],exist:[3,8,14,34],exit:[8,10],experi:[13,23,32],experimentcor:[15,23],explain:[3,22,33,34],explicitli:25,extend:10,extens:3,extent:21,extern:[6,11,14],f21b97ae83e8:12,fab:3,fail:[10,14],fairli:29,famou:30,fca4c231139f:12,feasibl:[19,32],featur:7,feel:[33,34],fernet:[5,12],fernet_kei:12,fetch:[4,9,12],field:[3,16],file:[4,5,6,7,8,9,10,13,14,22,23,26,27,30,33,35],filenam:[13,14],filesystem:4,filter:[3,8,13,33],find:[6,10,13,30],finish:[5,16,19],first:[3,4,5,11,22,23,25,27,30,31],first_nam:16,firstnam:33,flask:[3,29,33],flask_apispec:14,flask_app:[5,33],flask_env:[5,33],flexibl:34,flo:12,flow:32,flower:[3,6,9,11,12],focus:5,folder:[5,8,10,23,33],follow:[3,5,6,7,8,10,11,13,16,22,25,26,30,33],forbidden:11,foreign:16,forget:33,form:[3,14,22,30],format:[8,13,23,25,27,30,31,34],formul:[30,31],found:[0,8,10,18,21],foundat:29,free:34,freedom:34,frequenc:8,from:[3,5,6,8,10,13,14,16,21,23,26,27,30,31,33],from_dict:[13,23],from_fil:27,from_json:13,frontend:10,full:[9,10],futur:3,gap:[25,30],gaprel:25,gcc:10,gcp:9,gener:[3,5,10,11,14,16,22,25,31],generate_schema:13,get:[3,8,13,14,16,21,23,26,35],get_all_cas:13,get_all_execut:13,get_all_inst:13,get_all_us:[13,16],get_api_for_id:13,get_data:13,get_default_solver_nam:13,get_log:[13,27],get_object:[13,23],get_one_cas:13,get_one_inst:13,get_one_us:[13,16],get_one_user_by_email:16,get_one_user_by_usernam:16,get_result:13,get_schema:[13,18],get_solut:[13,27],get_solv:13,get_statu:[13,27],gevent:5,git:[26,33],github:[5,19,24,33],githubusercont:[4,9,12,33],give:[3,10,11,14,29,30],given:[10,16,23,30],glanc:8,goe:10,going:[3,14,21],good:[3,11,20],got:16,grade:11,grant:9,graph:[18,25,28,31],graph_color:[8,17],graph_coloring_input:8,graph_coloring_output:8,grep:33,group:[3,4],guarante:19,gui:[10,33],guid:[28,30],guidelin:25,gunicorn:5,gurobi:[29,31],hackathon:[18,28],hackathonbaobab2020:[8,19],had:25,handl:[0,3,8,29],happen:10,hardwar:12,has:[3,5,9,10,11,14,16,29,30],hash:16,have:[3,4,5,6,8,9,10,11,12,14,16,19,20,23,25,29,33,34],header:13,health:8,healthi:[4,8,12],help:[8,32],here:[3,8,12,23,25,31,33],heurist:[19,20,34],hierarchi:3,high:8,him:3,his:3,hk_2020_dag:[8,19],horizon:19,host:[4,5,10,11,12],host_databas:10,how:[3,11,28,34],http:[0,4,9,11,12,13,14,19,22,25,27,33],http_upgrad:11,human:16,hve:14,idcustom:25,ideal:23,identif:3,identifi:3,idtrail:25,idx:[14,16],imag:[3,4,6,10,12,33],immut:6,implement:[19,20,23],impli:34,includ:[2,5,6,10,13,14,18,22,23,25,26,29,31],independ:33,index:25,indistinctli:21,individu:[3,18],inexact:30,info:[8,14],inform:[3,5,7,8,9,12,13,14,16,22,23,25,29,30],infrastructur:6,inherit:16,init:33,initairflow:[4,12],initapp:[4,5,12],initi:[4,5,13,33],input:[13,23,24,25,26,30,34],insid:[5,8,13,21,22,23],instal:[3,5,6,7,8,10,12,28,32],instanc:[0,3,7,8,12,13,15,22,24,27,29,31,32],instance_id:[13,16,27],instance_solut:13,instancecor:[15,23],instancedataendpoint:14,instancedetailsendpoint:14,instancedetailsendpointbas:14,instanceendpoint:14,instancefileendpoint:14,instancemodel:[14,16],instancesolut:15,instancesolutioncor:13,instead:33,instruct:[28,32],integ:[14,25],intend:22,interact:[6,33],interfac:[13,21,34],intern:[3,6,10,11,14],interrupt:13,introduct:[28,32],invalidusag:13,involv:3,is_al:13,item:25,iterator_hl:19,its:[3,14,16,22,29,34],itself:[3,11,33],job:[3,11,12,19],json:[8,11,13,16,22,23,24,28,30,31,34],just:[9,22,23,30,35],keep:[3,5],kei:[3,5,11,12,16,23,25],kill:32,kind:[9,12,30],knapsack:30,know:[8,23,29],known:[6,25,28],kubernet:[5,6],kubernetesexecutor:5,kvappli:23,kwarg:[13,14,23],label:5,lambda:23,last:[3,16,19],last_nam:16,lastnam:33,latest:[5,8,33],launch:[5,8,32],layer:3,ldap:6,ldap_bind_dn:3,ldap_bind_password:3,ldap_email_attribut:3,ldap_group_attribut:3,ldap_group_bas:3,ldap_group_object_class:3,ldap_group_to_role_admin:3,ldap_group_to_role_plann:3,ldap_group_to_role_servic:3,ldap_group_to_role_view:3,ldap_host:3,ldap_use_tl:3,ldap_user_bas:3,ldap_user_object_class:3,ldap_user_typ:3,ldap_username_attribut:3,ldapv3:3,ldif:10,lead:11,learn:[9,11,33],least:[3,10,17,23],len:23,let:[8,25],level:8,lfo:[4,9,12],lib:[5,8],libpq:10,librari:[2,3,29],licens:29,life:5,like:[5,9,25,26,34],limit:30,line:[10,22,31],link:[3,5,14,16,33],linux:[4,8,10,33],list:[3,13,14,16,18,22,23,24,33],listen:[9,11],load:26,load_json:23,local:[5,8,10,24,33],local_path_to_dock:10,local_task_job:8,localhost:[4,9,11,12,33],localsolv:[31,34],locat:[9,10,11,23],log:[6,13,14,16,21,22,27,28,29,31,33],log_json:16,log_text:16,logging_mixin:8,login:[3,10,13,15,16,27],loginendpoint:14,logrot:8,look:[8,25,26],loop_ej:19,lose:34,loss:11,lucki:33,mac:7,machin:[10,12,26,29,33],made:[9,14,25],mai:[3,7,8,10],main:[5,12,28,29,34],mainli:19,maintain:[5,29],make:[3,4,9,11,14,23,25,30,31],make_admin:14,manag:[0,6,10,11,12,14,29,33],mandatori:[13,25],mang:10,mani:[12,20,22,23,34],manual_execut:13,mark:8,master:[3,4,9,12],match:[4,13,29,31],matheurist:19,max:20,mean:[11,25],measur:25,mechan:8,meet:7,member:3,memori:7,menu:35,merg:26,messag:[8,11,12,14,16],met:10,meta_model:16,meta_resourc:14,metaheurist:34,metaresourc:14,method:[3,6,13,14,16,17,19,20,24,25,28,29,32,34],methodolog:6,methodresourc:14,might:21,migrat:[3,5],mind:3,minim:[13,14,20,33],minimalist:[22,25],minimum:7,minut:[4,12],mip:[19,25,34],miss:10,missing_nod:23,missing_posit:23,mkdir:4,mode:[5,12,19],model:[3,15,17,19,20,28,31,34],modif:3,modifi:[10,26],moment:[5,11],monitor:[6,28],more:[3,5,7,8,9,11,12,22,23,33,34],mosek:31,most:[2,22,25,30],mount:[4,5,8,10],mps:14,much:8,multi:3,multipl:[11,12],must:[3,8,9,12,25,26],my_host:9,my_project:[26,27],myairflowurl:9,myairflowus:9,myairflowuserpwd:9,myapp:26,mycornflowpassword:9,mycornflowsit:11,mycornflowurl:9,mycornflowus:9,myorg:9,myproject:26,myredispassword:11,myserverip:[9,11],myserverport:9,mysit:11,myuser:[9,11],myuserpwd:[9,11],naiv:[23,25],name:[3,4,5,8,9,10,12,13,14,16,17,18,19,20,23,24,25,27,30],nativ:4,natur:30,navig:8,necessari:[3,4,5,7,11],necessarili:13,need:[3,4,7,8,11,12,16,18,21,22,23,25,26,30],neighbor:20,nest:24,network:3,never:[3,17,30],nevertheless:25,newer:7,newli:14,next:5,nginx:[9,11],node:[17,23,25],nodes_in:23,nodes_out:23,nomenclatur:29,non:19,none:[8,13],normal:10,nosolverexcept:13,note:[8,21,25],noth:16,now:[3,4,34],number:[8,12,13,17,30],object:[3,8,13,14,17,19,24,30,31],objectclass:3,obtain:[3,8],ofa:14,off:11,offer:[6,8,34],offici:[6,8,9,29],older:7,onc:[3,8,19,22,26,27],one:[3,5,10,13,14,16,19,22,23,30,31,34],ones:[3,14],ongo:[13,14],onli:[3,14,23,25,26,27,33],open:29,openldap:[10,11],oper:3,operationalerror:10,optim:[32,34],optim_dag:8,option:[6,13,16,23,28,33],order:[16,18,20,25,26,29],org:[22,25,29,33],organ:11,orlog:33,ornflow:26,ortool:[17,19,20,34],other:[3,6,11,13,14,19,23,26,30,31,33,34],otherwis:30,our:[21,25],ourselv:8,out:[3,14],output:[8,23,24,26,30,34],over:[3,23],overwritten:23,own:[3,28,29,34],owner:16,packag:[5,8,23,27,29],page:[8,9,11,18,21],pai:3,pair:[19,25],paragraph:30,parallel:12,param:13,paramet:[13,14,16,25],parent:[13,16],parent_id:13,pars:[10,13,16],particular:[13,14,25,30,33,34],pass:[3,8,14,23],password:[3,5,9,10,11,13,14,16,33],patch:13,patch_api_for_id:13,patch_one_cas:13,path:[5,8,10,13,23,27],pathtocertif:11,pathtocertificatekei:11,paus:21,payload:13,per:19,perform:[3,5,26],period:19,perman:8,permiss:[3,4,11],persist:[5,8],person:[6,30,33],pg_config:10,pip3:33,pip:[8,33],pkg:10,place:[3,11],placehold:35,plan:19,planner1234:11,planner:[3,11],platform:[3,6,10,11],pleas:[3,7,9,11],plenti:28,point:[3,11],popul:10,popular:5,port:[3,4,5,9,12],pos:[23,25],pose:30,posit:[23,25],posixaccount:3,possibl:[3,8,10,25,26,30],post:[3,13,14],post_api_for_id:13,post_url:13,postgr:[4,9,10,11,12],postgres_cf_data:5,postgres_db:5,postgres_password:5,postgres_us:5,postgresql:[6,11,33],preced:19,precis:6,prepar:[4,10],present:22,previou:[3,5,25],previous:[3,10,13,25],primari:16,prime:30,print:[27,33],privat:34,privileg:[3,9,14],problem:[6,13,17,18,22,23,25,26,28,29,31,32,34],procedur:30,process:[3,22,33],processor:29,produc:[13,25,26],product:[3,5,6,28],profil:[3,14],progress:[0,16],project:[5,6,26,28,29,31,33,34],proof:30,properli:[7,10],properti:[13,18,24],propos:[25,34],protocol:[3,11],prototyp:34,prove:30,provid:[3,6,8,12,16,25,30],proxi:[6,11],proxy_http_vers:11,proxy_pass:[9,11],proxy_redirect:11,proxy_set_head:11,psql:9,psycopg2:10,pull:[5,32,34],pulp:33,pure:[25,34],put:[11,13,14,18,19,22,23],put_api_for_id:13,put_one_cas:13,pwd:[5,13,33],pyomo:[19,34],python3:[5,8,26,33],python:[1,8,10,22,24,28,29,31,33,34],python_vers:33,pytup:23,queri:16,question:30,quit:30,quot:30,rang:23,rapid:34,raw:[4,9,12,33],reach:10,read:[3,10,11,34],readabl:16,readi:[11,26],real:[25,35],receiv:3,recommend:11,record:8,recov:19,redi:[11,12],redirect:9,redis_password:11,reduc:19,refer:[7,21,28,29,30],reference_id:[13,14],regard:3,register_act:10,register_base_assign:10,register_rol:10,register_view:10,regular:22,rel:25,relat:[3,12,14],relationship:[16,19],remaind:30,rememb:3,remot:31,remov:[4,12],renew:19,repositori:[5,6,10,11,18,19,26,31,33],repres:[3,13,16,25,29,30],represent:13,req_data:14,request:[3,9,10,11,13,34],requir:[4,5,6,7,9,14,16,22,23,24,32],resolut:[5,6,28],resourc:[7,12,13,19],rest:[0,3,8,28,29],restrict:[3,11],result:[13,14,16,29],retriev:29,revers:[6,11],review:8,rewrit:11,rfc:3,right:3,rmi:[4,12,33],role:[6,11,33],roles_with_access:14,root:[5,10],rotat:8,rout:[18,23,25,28],run:[0,3,5,6,7,11,14,21,25,26,28,29,33],rundag:29,runserv:10,safe:[3,5,11],sai:[8,21],said:6,salesman:30,samba:3,sambasamaccount:3,same:[3,10,12,14,16,17,26,33,34],sat:[17,19,20],save:[3,8,21,29],saw:3,scale:12,scenario:11,sch:12,schedul:[6,18,20,28,33],schema:[3,13,18,24,26,27,28,29,30,31,34],screen:25,script:[5,10,33],search:[3,8,33],second:[3,4,12,22,25,30,31],secret:[5,11],secret_kei:[5,33],section:[2,3,5,7,10,18,23,33,34],secuentialexecutor:5,secur:[3,6,28],see:[10,11,12,18,21,23,28,29,33,34],seed:25,select:29,self:[13,23,26],send:[3,21,29,31],sent:3,separ:[9,22,23],sequenc:[19,25],sequenti:5,sequentialexecutor:[5,33],serv:[23,29],server:[0,5,8,11,12,13,14,21,27,28,31,32,34],server_nam:[9,11],servic:[4,5,6,8,10,11,12,32,33],service_us:3,servicecornflow1234:3,session:[10,14],set:[3,5,9,11,13,23,29,30,33],setup:[6,11,26,32],sever:[22,23,31,33,34],sha256:16,share:[11,17],shell:10,should:[4,8,9,11,12,23,25,26,29,30],show:[0,10,31],shown:[8,25],sign:[13,14],sign_up:[13,27],signup:15,signupendpoint:14,similar:23,similarli:22,simpl:[19,24],simpli:8,simultan:[5,6,28],sinc:[2,3,6,8,30],singl:14,site:[8,29],situat:6,size:8,slapd:10,sleep:27,slim:5,small:23,solut:[3,9,10,14,15,17,19,20,24,28,29,31,32,34],solution_status_feas:13,solution_status_infeas:13,solutioncor:[15,23],solv:[3,10,15,19,20,22,23,25,26,29,31,32],solve_model_dag:[8,13],solver:[13,17,18,20,24,25,26,27,29,31,34],solvingtest:26,some:[3,10,25,26,29,30,34],someth:[11,21,26],sometim:[30,34],sort:[23,25],sourc:[26,33],spa:[0,1,28,29],space:32,specif:31,specifi:31,sqlalchemi:10,sqlite:33,src:[5,8],ssl:6,ssl_certif:11,ssl_certificate_kei:11,stack:[6,28],standard:[29,31],start:[4,5,10,11,19,28,33],start_dat:8,state:[16,27],state_messag:16,statist:0,statu:[4,8,12,14,15,16,29],status_cod:13,status_infeas:13,status_memory_limit:13,status_node_limit:13,status_not_solv:13,status_optim:13,status_time_limit:13,status_unbound:13,status_undefin:13,stdout:8,step:[7,30],still:[25,27],stop:[6,12,33],stop_execut:13,storag:[3,8],store:[3,5,8,11,13,16,22,23,29,30],str:[13,14,16],string:[14,16,22,25],structur:[13,14,16,24],stuff:3,sub:23,subclass:[23,30],subfold:8,submit:22,subtre:3,succesfulli:17,success:[8,14],sudo:[9,10],suffici:30,sum:23,superadmin:[9,14],superdict:23,superus:[5,9,14],support:[3,7,8,11,28],sure:[4,11,22,26],system:[3,6,11],tabl:[3,25],tag:5,tail:8,tailor:[25,30],take:[12,14,17,20,21,22,25,30],taken:12,task:[3,8,11,19,29],task_id:8,taskinst:8,tcp:[4,12],techniqu:34,technolog:6,templat:[6,9,11,12,13,23],temporari:3,termin:4,test1:13,test:[6,24,28,33,34],test_cas:[13,22,23,26],test_dag:26,test_my_project:27,test_solve_algo_1:26,test_try_solving_testcas:26,text:[16,22],than:[3,10,23,30,34],thei:[3,23,33],them:[3,8,14,21,23,26,29,33],themselv:26,theori:30,therefor:11,thi:[2,3,5,6,8,9,10,11,12,13,14,16,18,19,20,22,23,25,26,30,33,34,35],thing:[8,22,25],thisneedstobechang:33,those:[3,10],though:[16,25],thought:6,three:[3,12,13,22,23,25],through:[3,6,9,10,11,12],thu:3,tie:30,time:[3,4,5,11,16,19,20,21,25,27,30,33],timehorizon:25,timelimit:[23,25,27],timer:8,to_dict:[13,23,27],to_json:13,to_set:23,to_storag:8,todai:8,togeth:30,toggleuseradmin:14,token:[3,10,12,13,14],toler:[25,30],too:30,tool:[7,22,23,31],top:29,topic:28,total:20,trace:16,traceattribut:16,trailerscapac:25,translat:[6,10],transport:3,travel:30,tree:13,trigger:21,tsp:[24,31],tspapp:23,tspnaiv:23,tupl:[13,14],tuplist:23,two:[3,5,8,19,22,25,29,30,33],txt:[4,5,22,33],type:[3,6,8,11,12,13,14,16,19,23,24,33],ubuntu:33,unabl:10,unhealthi:4,unidimension:25,uniqu:[3,23],unit:[22,23,26],unittest:[2,22,26],unknown:13,until:[3,5],updat:[3,10,16,24,33],update_all_schema:[8,21],update_all_squema:8,update_st:16,update_view:10,updated_at:16,upgrad:[5,11,33],upload:[13,14,22,26],upon:[16,30],url:[5,13,14],usabl:34,usag:[10,32],use:[3,4,7,8,9,10,11,12,14,17,18,20,21,22,23,25,26,27,29,31,33,34],used:[0,3,5,12,13,14,16,18,22,23,25,29,30,32],useful:25,user:[0,4,5,6,9,10,13,15,18,28,29,33,34],user_id:[13,14,16],userdetailsendpoint:14,userendpoint:14,usermodel:16,usernam:[3,5,11,13,14,16,33],userwarn:8,uses:[5,21,29,34],using:[3,5,7,8,11,16,25,31],usr:[5,8],usual:[2,23,25,29],utc:16,valid:[3,14,22,25,26,29,30,34],valu:[3,8,10,11,12,13,16,25,30],vappli:23,variabl:[3,6,8,9,10,11,12,21,22],variant:20,varieti:8,variou:6,vehicl:[18,28],venv:33,veri:[5,23,31,34],version:[7,33],via:[3,29,34],view:[8,14],viewer1234:11,viewer:[3,11],virtual:33,visibl:3,visit:[8,9,25],visual:[0,8],volum:[4,5,8,10,12,33],vrp:20,vuej:0,wai:[3,5,6,8,10,25,30,31,32],wait:27,want:[3,5,8,9,11,12,19,21,23,26,33,34],warn:8,web:[1,4,10,12,14,21,28,29,31,33],webserv:[3,6,9,14,16,33],weight:[23,25],welcom:28,well:[8,25,31],were:10,what:[21,34],when:[3,5,10,11,16,18,19,21,22,23,26,30],where:[5,8,20],whether:[26,30],which:[3,5,6,8,10,14,19,23,25,29,30,34],who:[3,11],whole:[17,19,22],whose:25,why:23,wikipedia:30,window:[7,33],wit:14,with_traceback:13,within:[3,8],without:[8,34],wor:12,work:[3,5,6,22,34,35],worker:[5,6,12,32,33],worker_:8,workflow:3,workstat:7,wors:30,would:[6,25,30],write:[13,14,22,23,24,28],write_solut:13,written:8,wsl:33,xml:27,yes:30,yml:[5,6,7,9,10,11,12,28,33],you:[2,3,4,5,6,8,9,10,11,12,21,23,26,27,28,33,34],your:[3,4,7,8,10,11,12,18,22,23,24,25,28,34],your_email:27,your_password:27,your_user_nam:27,yourpathtofilerequir:4,zero:30,zip:23},titles:["Admin client","Supported clients","Python API","Access control","docker-compose.yml","Docker stack","Deploy your own Cornflow-server","Before you begin","Logging and monitoring","Deployment options","Known problems","Production deployment and security","Running with simultaneous resolutions","Cornflow-client","Endpoints","Code documentation","Models","Graph coloring","Examples of solution methods","Scheduling: hackathon","Vehicle Routing Problem","Debug your solution method","How to deploy a new solution method","How to deploy a new solution method (2.0)","User guides and how-to","Write a json-schema","Test your solution method","User your solution method","Cornflow documentation","Cornflow-server architecture","Concepts","Examples","Main topics","Installation instructions","Introduction","REST API Reference"],titleterms:{"case":[22,23,31],"class":[13,23],"default":3,"new":[22,23],The:22,Use:31,With:3,__init__:23,access:3,admin:0,airflow:[3,5,8,9,10,11,29,33],api:[2,35],applic:23,applicationcor:13,architectur:29,auth:3,authent:[3,11],backend:11,basic:[25,26],befor:7,begin:7,build:[5,10,33],can:34,clean:4,client:[0,1,13,27,29],code:[15,23],color:17,common:21,complet:23,compon:29,compos:4,concept:30,configur:[25,30,33],connect:9,constant:13,control:3,core:13,cornflow:[3,4,6,8,9,10,13,21,28,29,33],dag:14,data:[3,29],databas:[9,10,11,33],debug:21,decis:30,definit:3,deploi:[6,22,23],deploy:[9,11],develop:10,docker:[4,5,10,33],document:[15,28],endpoint:14,enforc:11,entrypoint:5,environ:[4,5],error:21,exampl:[18,25,31],except:25,execut:[14,16,30],experi:30,experimentcor:13,extern:3,feasibl:30,flow:29,flower:10,github:26,graph:17,guid:24,hackathon:19,help:33,how:[22,23,24],imag:5,input:22,instal:33,instanc:[14,16,23,25,30],instancecor:13,instancesolut:13,instruct:33,interact:3,introduct:34,json:25,kill:33,known:10,launch:33,ldap:[3,10,11],list:25,local:26,log:8,login:14,main:32,manag:3,method:[18,21,22,23,26,27,30],model:16,monitor:8,name:22,nest:25,object:25,offici:5,optim:30,option:9,output:22,own:[6,9],person:5,postgresql:[5,9],problem:[10,20,30],product:11,properti:[23,25],proxi:9,pull:33,python:[2,27],refer:35,requir:[3,25,33],resolut:12,rest:35,revers:9,role:3,rout:20,run:[4,9,10,12],schedul:[8,19],schema:[21,22,23,25],secur:11,server:[3,6,9,10,29,33],servic:[3,29],setup:[9,33],signup:14,simpl:25,simultan:12,situat:10,solut:[13,18,21,22,23,25,26,27,30],solutioncor:13,solv:[13,30],solver:[22,23],space:30,ssl:11,stack:5,statu:13,stop:4,structur:23,support:1,test:[22,23,26],topic:32,tsp:[23,25],type:25,updat:21,usag:33,used:34,user:[3,11,14,16,24,27],variabl:5,vehicl:20,wai:34,worker:[8,29],write:25,yml:4,you:7,your:[6,9,21,26,27]}})