WAGON=custom_plugin_test_stp_name-1.0-py27-none-manylinux1_x86_64-centos-Core.wgn
BLUEPRINT=blueprint_test_plugin.yaml
CONTAINER=cfy_manager_local
FOLDER=plugin
RANDOM=$$
NAME="blueprint-plugin-"

CMD="docker exec ${CONTAINER} "
echo "Upload plugin to CFY"
${CMD} cfy plugins upload ${WAGON} -y ${FOLDER}.yaml
echo "Upload blueprint ${RANDOM} to CFY"
echo "CMD: ${CMD} cfy blueprint upload ${BLUEPRINT} -b ${NAME}${RANDOM}"
${CMD} cfy blueprint upload -b ${NAME}${RANDOM} /${BLUEPRINT}
