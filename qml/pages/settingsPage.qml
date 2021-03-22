import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

Item {
    Rectangle {
        id: rectangle
        color: "#2c313c"
        anchors.fill: parent

        Label {
            id: label
            color: "#ffffff"
            text: qsTr("Preferences")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.family: "Times New Roman"
            font.italic: false
            font.bold: false
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 10
            styleColor: "#000000"
            font.pointSize: 26
        }

        Rectangle {
            id: rectangle1
            height: 38
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: label.bottom
            anchors.rightMargin: 20
            anchors.leftMargin: 50
            anchors.topMargin: 50

            CheckBox {
                id: unlockStartup
                width: 47
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                spacing: 25
                indicator: Rectangle {
                    x: unlockStartup.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: unlockStartup.down ? "#17a81a" : "#21be2b"
                    implicitHeight: 26
                    Text {
                        visible: unlockStartup.checked
                        color: unlockStartup.down ? "#17a81a" : "#21be2b"
                        text: "\u2714"
                        anchors.fill: parent
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        fontSizeMode: Text.FixedSize
                        font.pointSize: 18
                    }
                    implicitWidth: 26
                }
                font.pointSize: 18
                font.weight: Font.Medium
            }

            Label {
                id: label2
                color: "#ffffff"
                text: qsTr("Unlock at startup")
                anchors.left: unlockStartup.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.family: "Times New Roman"
                anchors.leftMargin: 0
                font.pointSize: 18
            }
        }

        Rectangle {
            id: rectangle2
            height: 38
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: rectangle1.bottom
            anchors.leftMargin: 50
            anchors.rightMargin: 20
            anchors.topMargin: 10

            CheckBox {
                id: lockOtherPerson
                width: 47
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                spacing: 25
                font.pointSize: 18
                font.weight: Font.Medium
                indicator: Rectangle {
                    implicitWidth: 26
                    implicitHeight: 26
                    x: lockOtherPerson.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: lockOtherPerson.down ? "#17a81a" : "#21be2b"

                    Text {
                        text: "✔"
                        anchors.fill: parent
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 18
                        color: lockOtherPerson.down ? "#17a81a" : "#21be2b"
                        visible: lockOtherPerson.checked

                    }
                }
            }

            Label {
                id: label1
                color: "#ffffff"
                text: qsTr("Lock when other person appears")
                anchors.left: lockOtherPerson.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.pointSize: 18
                font.family: "Times New Roman"
                anchors.leftMargin: 0
            }



        }

        Rectangle {
            id: rectangle3
            height: 38
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: rectangle2.bottom
            anchors.leftMargin: 50
            anchors.rightMargin: 20
            anchors.topMargin: 10
            CheckBox {
                id: lockOtherPerson1
                width: 47
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                spacing: 25
                indicator: Rectangle {
                    x: lockOtherPerson1.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: lockOtherPerson1.down ? "#17a81a" : "#21be2b"
                    implicitHeight: 26
                    Text {
                        visible: lockOtherPerson1.checked
                        color: lockOtherPerson1.down ? "#17a81a" : "#21be2b"
                        text: "\u2714"
                        anchors.fill: parent
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 18
                    }
                    implicitWidth: 26
                }
                font.pointSize: 18
                font.weight: Font.Medium
            }

            Label {
                id: label3
                color: "#ffffff"
                text: qsTr("Auto Lock when you are not there")
                anchors.left: lockOtherPerson1.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.family: "Times New Roman"
                anchors.leftMargin: 0
                font.pointSize: 18
            }
        }

        Rectangle {
            id: rectangle4
            height: 38
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: rectangle3.bottom
            anchors.leftMargin: 50
            anchors.rightMargin: 20
            anchors.topMargin: 10
            CheckBox {
                id: lockOtherPerson2
                width: 47
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                spacing: 25
                indicator: Rectangle {
                    x: lockOtherPerson2.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: lockOtherPerson2.down ? "#17a81a" : "#21be2b"
                    implicitHeight: 26
                    Text {
                        visible: lockOtherPerson2.checked
                        color: lockOtherPerson2.down ? "#17a81a" : "#21be2b"
                        text: "\u2714"
                        anchors.fill: parent
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 18
                    }
                    implicitWidth: 26
                }
                font.pointSize: 18
                font.weight: Font.Medium
            }

            Label {
                id: label4
                color: "#ffffff"
                text: qsTr("Auto unlock when you are there")
                anchors.left: lockOtherPerson2.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.family: "Times New Roman"
                anchors.leftMargin: 0
                font.pointSize: 18
            }
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}D{i:2}D{i:6}D{i:3}D{i:11}D{i:8}D{i:13}D{i:18}
}
##^##*/
