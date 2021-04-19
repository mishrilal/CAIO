import QtQuick 2.15
import QtQuick.Controls 2.15
import "../controls"


Item {
    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent

        Rectangle {
            id: logBtnContainer
            height: 50
            color: "#16181d"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
            Rectangle{
                anchors{
                    left: parent.left
                    right: parent.right
                    bottom: parent.bottom
                }
                color: "#2c313c"
                height: 5
                visible: true
            }

            Rectangle {
                id: rectangle1
                width: 600
                color: "#ffffff"
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: parent.horizontalCenter

                LogsBtn{
                    id: allLogsBtn
                    text: "All Logs"
                    isActiveMenu: true
                    onClicked: {
                        allLogsPage.active = true
                        adminLogsPage.active = false
                        someoneLogsPage.active = false
                        nobodyLogsPage.active = false

                        allLogsBtn.isActiveMenu = true
                        adminLogsBtn.isActiveMenu = false
                        someoneLogsBtn.isActiveMenu = false
                        nobodyLogsBtn.isActiveMenu = false

                        allLogsPage.visible = true
                        adminLogsPage.visible = false
                        someoneLogsPage.visible = false
                        nobodyLogsPage.visible = false

                    }

                }

                LogsBtn{
                    id: adminLogsBtn
                    isActiveMenu: false
                    x: 150
                    y: 0
                    text: "Admin Logs"
                    anchors.left: allLogsBtn.right
                    anchors.leftMargin: 0
                    onClicked: {
                        allLogsPage.active = false
                        adminLogsPage.active = true
                        someoneLogsPage.active = false
                        nobodyLogsPage.active = false

                        allLogsBtn.isActiveMenu = false
                        adminLogsBtn.isActiveMenu = true
                        someoneLogsBtn.isActiveMenu = false
                        nobodyLogsBtn.isActiveMenu = false

                        allLogsPage.visible = false
                        adminLogsPage.visible = true
                        someoneLogsPage.visible = false
                        nobodyLogsPage.visible = false

                    }

                }

                LogsBtn{
                    id: someoneLogsBtn
                    isActiveMenu: false
                    x: 300
                    y: 0
                    text: "Someone Logs"
                    anchors.left: adminLogsBtn.right
                    anchors.leftMargin: 0
                    onClicked: {
                        allLogsPage.active = false
                        adminLogsPage.active = false
                        someoneLogsPage.active = true
                        nobodyLogsPage.active = false

                        allLogsBtn.isActiveMenu = false
                        adminLogsBtn.isActiveMenu = false
                        someoneLogsBtn.isActiveMenu = true
                        nobodyLogsBtn.isActiveMenu = false

                        allLogsPage.visible = false
                        adminLogsPage.visible = false
                        someoneLogsPage.visible = true
                        nobodyLogsPage.visible = false

                    }

                }

                LogsBtn{
                    id: nobodyLogsBtn
                    isActiveMenu: false
                    x: 450
                    y: 0
                    text: "Nobody Logs"
                    anchors.left: someoneLogsBtn.right
                    anchors.leftMargin: 0
                    onClicked: {
                        allLogsPage.active = false
                        adminLogsPage.active = false
                        someoneLogsPage.active = false
                        nobodyLogsPage.active = true

                        allLogsBtn.isActiveMenu = false
                        adminLogsBtn.isActiveMenu = false
                        someoneLogsBtn.isActiveMenu = false
                        nobodyLogsBtn.isActiveMenu = true

                        allLogsPage.visible = false
                        adminLogsPage.visible = false
                        someoneLogsPage.visible = false
                        nobodyLogsPage.visible = true

                    }

                }
            }
        }

        Rectangle {
            id: logsContainer
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: logBtnContainer.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0

            Loader{
                id: allLogsPage
                anchors.fill: parent
                source: Qt.resolvedUrl("allLogsPage.qml")
                active: true
                visible: true
            }
            Loader{
                id: adminLogsPage
                anchors.fill: parent
                source: Qt.resolvedUrl("adminLogsPage.qml")
                active: false
                visible: false
            }

            Loader{
                id: someoneLogsPage
                anchors.fill: parent
                source: Qt.resolvedUrl("someoneLogsPage.qml")
                active: false
                visible: false
            }

            Loader{
                id: nobodyLogsPage
                anchors.fill: parent
                source: Qt.resolvedUrl("nobodyLogsPage.qml")
                active: false
                visible: false
            }



        }


    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:3}
}
##^##*/
