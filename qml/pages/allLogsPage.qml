import QtQuick 2.15
import QtQuick.Controls 2.15


Item {
    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent

        Rectangle {
            id: logContainer
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 10
            anchors.leftMargin: 10
            anchors.bottomMargin: 0
            clip: true
            anchors.topMargin: 10

            ScrollView {
                id: scrollView
                anchors.fill: parent

                TableView {
                    id: allLogsView
                    anchors.fill: parent
                    columnSpacing: 1
                    rowSpacing: 1
                    boundsBehavior: Flickable.StopAtBounds

                    model: tableModel

                    delegate:  Text {
                        text: model.display
                        font.family: "Times New Roman"
                        font.pointSize: 14
                        clip: true
                        padding: 6
                        color: "#ffffff"

                        Rectangle {
                            color: "#00000000"
                            border.color: "#00000000"
                            border.width: 1
                            anchors.fill: parent
                            transformOrigin: Item.TopLeft
                            clip: true
                            z: -1
                        }

                        Rectangle{
                            height: 1
                            border.width: 2
                            width: parent.width
                        }
                    }

                }
            }
        }
    }

    Connections {
        target: backend
    }
}
/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
