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

                onClicked: {
                    settingsBackend.startupClicked(checked)
                    print("QML Startup")
                }
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
                onClicked: {
                    settingsBackend.lockOther(checked)
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
                id: autoLock
                width: 47
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                spacing: 25
                indicator: Rectangle {
                    x: autoLock.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: autoLock.down ? "#17a81a" : "#21be2b"
                    implicitHeight: 26
                    Text {
                        visible: autoLock.checked
                        color: autoLock.down ? "#17a81a" : "#21be2b"
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
                onClicked: {
                    settingsBackend.autoLock(checked)
                }
            }

            Label {
                id: label3
                color: "#ffffff"
                text: qsTr("Auto Lock when you are not there")
                anchors.left: autoLock.right
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
                id: autoUnlock
                width: 47
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                spacing: 25
                indicator: Rectangle {
                    x: autoUnlock.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: autoUnlock.down ? "#17a81a" : "#21be2b"
                    implicitHeight: 26
                    Text {
                        visible: autoUnlock.checked
                        color: autoUnlock.down ? "#17a81a" : "#21be2b"
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

                onClicked: {
                    settingsBackend.autoUnlock(checked)
                }
            }

            Label {
                id: label4
                color: "#ffffff"
                text: qsTr("Auto unlock when you are there")
                anchors.left: autoUnlock.right
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

    Connections {
        target: settingsBackend;

        function onSetStartup(value) {
            unlockStartup.checked = value
            print(value)
        }


    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}
}
##^##*/
