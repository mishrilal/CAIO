import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt.labs.qmlmodels 1.0
import "../controls/"

Item {
    id: item1
    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent

        Label {
            id: label
            color: "#ffffff"
            text: qsTr("DashBoard Page")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 10
            font.pointSize: 16
        }

        Rectangle {
            id: rectangle1
            color: "#00000000"
            anchors.fill: parent
            anchors.topMargin: 40

            Rectangle {
                id: leftSide
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: parent.width / 3

                Rectangle {
                    id: rectangle2
                    height: parent.height / 2
                    color: "#00000000"
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.verticalCenterOffset: -30
                    anchors.rightMargin: 0
                    anchors.leftMargin: 20

                    Rectangle {
                        id: rectangleLeft
                        height: (rectangle2.width / 3) - 10
                        color: "#00000000"
                        width: (rectangle2.width / 3) - 10
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 5
                        CircularProgress {
                            id: circularProgressLeft
                            text: " "
                            anchors.fill: parent
                            infoText: "Locks When Admin is Not present"
                        }

                    }
                    Rectangle {
                        id: rectangleCenter
                        height: (rectangle2.width / 3) - 10
                        color: "#00000000"
                        width: (rectangle2.width / 3) - 10
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: rectangleLeft.right
                        anchors.right: rectangleRight.left
                        anchors.rightMargin: 5
                        anchors.leftMargin: 5
                        CircularProgress {
                            id: circularProgressCenter
                            text: " "
                            anchors.fill: parent
                            infoText: "Locks When SomeOne came"
                        }

                    }
                    Rectangle {
                        id: rectangleRight
                        height: (rectangle2.width / 3) - 10
                        color: "#00000000"
                        width: (rectangle2.width / 3) - 10
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.rightMargin: 5
                        CircularProgress {
                            id: circularProgressRight
                            text: " "
                            anchors.fill: parent
                            infoText: "Locks When nobody is there"
                        }

                    }

                }

            }

            Rectangle {
                id: rightSide
                color: "#00000000"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                clip: true
                anchors.leftMargin: parent.width - parent.width / 3

                Label {
                    id: label1
                    color: "#ffffff"
                    text: qsTr("LOGS")
                    font.pointSize: 14
                    font.family: "Times New Roman"
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                Rectangle {
                    id: logContainer
                    color: "#00000000"
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: label1.bottom
                    anchors.bottom: parent.bottom
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 0
                    clip: true
                    anchors.topMargin: 10

                    ScrollView {
                        id: scrollView
                        anchors.fill: parent

                        //                        TableView {
                        //                                anchors.fill: parent
                        //                                columnSpacing: 1
                        //                                rowSpacing: 1
                        //                                boundsBehavior: Flickable.StopAtBounds

                        //                                model: TableModel {
                        //                                    TableModelColumn { display: "checked" }
                        //                                    TableModelColumn { display: "amount" }
                        //                                    TableModelColumn { display: "fruitType" }
                        //                                    TableModelColumn { display: "fruitName" }
                        //                                    TableModelColumn { display: "fruitPrice" }



                        //                                    // Each row is one type of fruit that can be ordered
                        //                                    rows: [
                        //                                        {
                        //                                            // Each property is one cell/column.
                        //                                            checked: false,
                        //                                            amount: 1,
                        //                                            fruitType: "Apple",
                        //                                            fruitName: "Granny Smith",
                        //                                            fruitPrice: 1.50
                        //                                        },
                        //                                        {
                        //                                            checked: true,
                        //                                            amount: 4,
                        //                                            fruitType: "Orange",
                        //                                            fruitName: "Navel",
                        //                                            fruitPrice: 2.50
                        //                                        },
                        //                                        {
                        //                                            checked: false,
                        //                                            amount: 1,
                        //                                            fruitType: "Banana",
                        //                                            fruitName: "Cavendish",
                        //                                            fruitPrice: 3.50
                        //                                        }
                        //                                    ]
                        //                                }
                        //                                delegate:  Text {
                        //                                    text: model.display
                        //                                    padding: 12

                        //                                    Rectangle {
                        //                                        anchors.fill: parent
                        //                                        color: "#efefef"
                        //                                        z: -1
                        //                                    }
                        //                                }
                        //                            }


                    }

                    Label {
                        id: label2
                        color: "#ffffff"
                        text: qsTr("Logs not recorded yet")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        anchors.topMargin: 20
                        renderType: Text.NativeRendering
                        visible: false
                    }
                }
            }
        }
    }

    Connections {
        target: dashboardBackend
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:6}D{i:8}D{i:10}D{i:5}
}
##^##*/
