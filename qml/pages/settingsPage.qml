import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import Qt.labs.settings 1.0

Item {
    Rectangle {
        id: rectangle
        color: "#16181d"
        border.width: 1
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
            id: leftRectangle
            color: "#00000000"
            border.width: 0
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: label.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: parent.width / 2
            anchors.leftMargin: 20
            anchors.topMargin: 10
//            Rectangle {
//                id: rectangle1
//                x: 40
//                y: 40
//                height: 38
//                color: "#00000000"
//                anchors.left: parent.left
//                anchors.right: parent.right
//                anchors.top: parent.top
//                anchors.rightMargin: 20
//                anchors.leftMargin: 0
//                anchors.topMargin: 10

//                CheckBox {
//                    id: autoUnlock
//                    width: 47
//                    anchors.left: parent.left
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    enabled: false
//                    checkable: true
//                    spacing: 25
//                    indicator: Rectangle {
//                        x: autoUnlock.leftPadding
//                        y: parent.height / 2 - height / 2
//                        radius: 3
//                        border.color: autoUnlock.down ? "#17a81a" : "#21be2b"
//                        implicitHeight: 26
//                        Text {
//                            visible: autoUnlock.checked
//                            color: autoUnlock.down ? "#17a81a" : "#21be2b"
//                            text: "\u2714"
//                            anchors.fill: parent
//                            horizontalAlignment: Text.AlignHCenter
//                            verticalAlignment: Text.AlignVCenter
//                            fontSizeMode: Text.FixedSize
//                            font.pointSize: 18
//                        }
//                        implicitWidth: 26
//                    }
//                    font.pointSize: 18
//                    font.weight: Font.Medium

//                    onClicked: {
//                        settingsBackend.autoUnlockClicked(checked)
//                    }
//                }

//                Label {
//                    id: label2
//                    color: "#ffffff"
//                    text: qsTr("Auto Unlock")
//                    anchors.left: autoUnlock.right
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    horizontalAlignment: Text.AlignLeft
//                    verticalAlignment: Text.AlignVCenter
//                    font.family: "Times New Roman"
//                    anchors.leftMargin: 0
//                    font.pointSize: 18
//                }
//            }

//            Rectangle {
//                id: rectangle2
//                x: 40
//                y: 88
//                height: 38
//                color: "#00000000"
//                anchors.left: parent.left
//                anchors.right: parent.right
//                anchors.top: rectangle1.bottom
//                anchors.leftMargin: 0
//                anchors.rightMargin: 20
//                anchors.topMargin: 10

//                CheckBox {
//                    id: onlyAdminStrict
//                    width: 47
//                    anchors.left: parent.left
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    autoRepeat: true
//                    spacing: 25
//                    font.pointSize: 18
//                    font.weight: Font.Medium
//                    indicator: Rectangle {
//                        implicitWidth: 26
//                        implicitHeight: 26
//                        x: onlyAdminStrict.leftPadding
//                        y: parent.height / 2 - height / 2
//                        radius: 3
//                        border.color: onlyAdminStrict.down ? "#17a81a" : "#21be2b"

//                        Text {
//                            text: "✔"
//                            anchors.fill: parent
//                            horizontalAlignment: Text.AlignHCenter
//                            verticalAlignment: Text.AlignVCenter
//                            font.pointSize: 18
//                            color: onlyAdminStrict.down ? "#17a81a" : "#21be2b"
//                            visible: onlyAdminStrict.checked

//                        }
//                    }
//                    onClicked: {
//                        settingsBackend.onlyAdminStrictClicked(checked)
//                        onlyAdmin.checked = false
//                        someoneAppears.checked = false
//                        someoneAppearsStrict.checked = false
//                    }
//                }

//                Label {
//                    id: label1
//                    color: "#ffffff"
//                    text: qsTr("Only Admin Strict")
//                    anchors.left: onlyAdminStrict.right
//                    anchors.right: parent.right
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    horizontalAlignment: Text.AlignLeft
//                    verticalAlignment: Text.AlignVCenter
//                    font.pointSize: 18
//                    font.family: "Times New Roman"
//                    anchors.leftMargin: 0
//                }



//            }

//            Rectangle {
//                id: rectangle3
//                x: 40
//                y: 136
//                height: 38
//                color: "#00000000"
//                anchors.left: parent.left
//                anchors.right: parent.right
//                anchors.top: rectangle2.bottom
//                anchors.leftMargin: 0
//                anchors.rightMargin: 20
//                anchors.topMargin: 10
//                CheckBox {
//                    id: onlyAdmin
//                    width: 47
//                    anchors.left: parent.left
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    spacing: 25
//                    indicator: Rectangle {
//                        x: onlyAdmin.leftPadding
//                        y: parent.height / 2 - height / 2
//                        radius: 3
//                        border.color: onlyAdmin.down ? "#17a81a" : "#21be2b"
//                        implicitHeight: 26
//                        Text {
//                            visible: onlyAdmin.checked
//                            color: onlyAdmin.down ? "#17a81a" : "#21be2b"
//                            text: "\u2714"
//                            anchors.fill: parent
//                            horizontalAlignment: Text.AlignHCenter
//                            verticalAlignment: Text.AlignVCenter
//                            font.pointSize: 18
//                        }
//                        implicitWidth: 26
//                    }
//                    font.pointSize: 18
//                    font.weight: Font.Medium
//                    onClicked: {
//                        settingsBackend.onlyAdminClicked(checked)
//                        onlyAdminStrict.checked = false
//                        someoneAppears.checked = false
//                        someoneAppearsStrict.checked = false
//                    }
//                }

//                Label {
//                    id: label3
//                    color: "#ffffff"
//                    text: qsTr("Only Admin or No one")
//                    anchors.left: onlyAdmin.right
//                    anchors.right: parent.right
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    horizontalAlignment: Text.AlignLeft
//                    verticalAlignment: Text.AlignVCenter
//                    font.family: "Times New Roman"
//                    anchors.leftMargin: 0
//                    font.pointSize: 18
//                }
//            }

//            Rectangle {
//                id: rectangle4
//                x: 40
//                y: 184
//                height: 38
//                color: "#00000000"
//                anchors.left: parent.left
//                anchors.right: parent.right
//                anchors.top: rectangle3.bottom
//                anchors.leftMargin: 0
//                anchors.rightMargin: 20
//                anchors.topMargin: 10
//                CheckBox {
//                    id: someoneAppearsStrict
//                    width: 47
//                    anchors.left: parent.left
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    spacing: 25
//                    indicator: Rectangle {
//                        x: someoneAppearsStrict.leftPadding
//                        y: parent.height / 2 - height / 2
//                        radius: 3
//                        border.color: someoneAppearsStrict.down ? "#17a81a" : "#21be2b"
//                        implicitHeight: 26
//                        Text {
//                            visible: someoneAppearsStrict.checked
//                            color: someoneAppearsStrict.down ? "#17a81a" : "#21be2b"
//                            text: "\u2714"
//                            anchors.fill: parent
//                            horizontalAlignment: Text.AlignHCenter
//                            verticalAlignment: Text.AlignVCenter
//                            font.pointSize: 18
//                        }
//                        implicitWidth: 26
//                    }
//                    font.pointSize: 18
//                    font.weight: Font.Medium

//                    onClicked: {
//                        settingsBackend.someoneAppearsStrictClicked(checked)
//                        onlyAdmin.checked = false
//                        onlyAdminStrict.checked = false
//                        someoneAppears.checked = false
//                    }
//                }

//                Label {
//                    id: label4
//                    color: "#ffffff"
//                    text: qsTr("Someone Appears Strict")
//                    anchors.left: someoneAppearsStrict.right
//                    anchors.right: parent.right
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    horizontalAlignment: Text.AlignLeft
//                    verticalAlignment: Text.AlignVCenter
//                    font.family: "Times New Roman"
//                    anchors.leftMargin: 0
//                    font.pointSize: 18
//                }
//            }

//            Rectangle {
//                id: rectangle5
//                x: 40
//                y: 232
//                height: 38
//                color: "#00000000"
//                anchors.left: parent.left
//                anchors.right: parent.right
//                anchors.top: rectangle4.bottom
//                CheckBox {
//                    id: someoneAppears
//                    width: 47
//                    anchors.left: parent.left
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    spacing: 25
//                    font.weight: Font.Medium
//                    indicator: Rectangle {
//                        x: someoneAppears.leftPadding
//                        y: parent.height / 2 - height / 2
//                        radius: 3
//                        border.color: someoneAppears.down ? "#17a81a" : "#21be2b"
//                        Text {
//                            visible: someoneAppears.checked
//                            color: someoneAppears.down ? "#17a81a" : "#21be2b"
//                            text: "\u2714"
//                            anchors.fill: parent
//                            horizontalAlignment: Text.AlignHCenter
//                            verticalAlignment: Text.AlignVCenter
//                            rotation: 0
//                            font.pointSize: 18
//                        }
//                        implicitWidth: 26
//                        implicitHeight: 26
//                    }
//                    onClicked: {
//                        settingsBackend.someoneAppearsClicked(checked)
//                        onlyAdmin.checked = false
//                        onlyAdminStrict.checked = false
//                        someoneAppearsStrict.checked = false
//                    }
//                    font.pointSize: 18
//                }

//                Label {
//                    id: label5
//                    color: "#ffffff"
//                    text: qsTr("Someone appears or no one")
//                    anchors.left: someoneAppears.right
//                    anchors.right: parent.right
//                    anchors.top: parent.top
//                    anchors.bottom: parent.bottom
//                    horizontalAlignment: Text.AlignLeft
//                    verticalAlignment: Text.AlignVCenter
//                    font.family: "Times New Roman"
//                    anchors.leftMargin: 0
//                    font.pointSize: 18
//                }
//                anchors.rightMargin: 20
//                anchors.leftMargin: 0
//                anchors.topMargin: 10
//            }

            CheckBox {
                id: onlyAdminStrict
                text: qsTr("CheckBox")
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.leftMargin: 0
                anchors.topMargin: 10

                indicator: Rectangle {
                    implicitWidth: 26
                    implicitHeight: 26
                    x: onlyAdminStrict.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: onlyAdminStrict.down ? "#17a81a" : "#21be2b"

                    Rectangle {
                        width: 14
                        height: 14
                        x: 6
                        y: 6
                        radius: 2
                        color: onlyAdminStrict.down ? "#17a81a" : "#21be2b"
                        visible: onlyAdminStrict.checked
                    }
                }

                contentItem: Text {
                    font: onlyAdminStrict.font
                    opacity: enabled ? 1.0 : 0.3
                    color: "#ffffff"
                    text: "Only Admin Strict"
                    verticalAlignment: Text.AlignVCenter
                    leftPadding: onlyAdminStrict.indicator.width + onlyAdminStrict.spacing
                }
                onClicked: {
                    settingsBackend.onlyAdminStrictClicked(checked)
                    onlyAdmin.checked = false
                    someoneAppears.checked = false
                    someoneAppearsStrict.checked = false
                }
            }

            CheckBox {
                id: onlyAdmin
                text: qsTr("CheckBox")
                anchors.left: parent.left
                anchors.top: onlyAdminStrict.bottom
                anchors.leftMargin: 0
                anchors.topMargin: 10
                indicator: Rectangle {
                    x: onlyAdmin.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: onlyAdmin.down ? "#17a81a" : "#21be2b"
                    implicitWidth: 26
                    implicitHeight: 26
                    Rectangle {
                        x: 6
                        y: 6
                        width: 14
                        height: 14
                        visible: onlyAdmin.checked
                        color: onlyAdmin.down ? "#17a81a" : "#21be2b"
                        radius: 2
                    }
                }
                contentItem: Text {
                    opacity: enabled ? 1.0 : 0.3
                    color: "#ffffff"
                    text: "Only Admin or No one"
                    verticalAlignment: Text.AlignVCenter
                    font: onlyAdmin.font
                    leftPadding: onlyAdmin.indicator.width + onlyAdmin.spacing
                }

                onClicked: {
                    settingsBackend.onlyAdminClicked(checked)
                    onlyAdminStrict.checked = false
                    someoneAppears.checked = false
                    someoneAppearsStrict.checked = false
                }
            }

            CheckBox {
                id: someoneAppearsStrict
                text: qsTr("CheckBox")
                anchors.left: parent.left
                anchors.top: onlyAdmin.bottom
                anchors.leftMargin: 0
                anchors.topMargin: 10
                indicator: Rectangle {
                    x: someoneAppearsStrict.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: someoneAppearsStrict.down ? "#17a81a" : "#21be2b"
                    implicitWidth: 26
                    implicitHeight: 26
                    Rectangle {
                        x: 6
                        y: 6
                        width: 14
                        height: 14
                        visible: someoneAppearsStrict.checked
                        color: someoneAppearsStrict.down ? "#17a81a" : "#21be2b"
                        radius: 2
                    }
                }
                contentItem: Text {
                    opacity: enabled ? 1.0 : 0.3
                    color: "#ffffff"
                    text: "Someone Appears Strict"
                    verticalAlignment: Text.AlignVCenter
                    font: someoneAppearsStrict.font
                    leftPadding: someoneAppearsStrict.indicator.width + someoneAppearsStrict.spacing
                }

                onClicked: {
                    settingsBackend.someoneAppearsStrictClicked(checked)
                    onlyAdmin.checked = false
                    onlyAdminStrict.checked = false
                    someoneAppears.checked = false
                }
            }

            CheckBox {
                id: someoneAppears
                text: qsTr("CheckBox")
                anchors.left: parent.left
                anchors.top: someoneAppearsStrict.bottom
                anchors.leftMargin: 0
                anchors.topMargin: 10
                indicator: Rectangle {
                    x: someoneAppears.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: someoneAppears.down ? "#17a81a" : "#21be2b"
                    implicitWidth: 26
                    implicitHeight: 26
                    Rectangle {
                        x: 6
                        y: 6
                        width: 14
                        height: 14
                        visible: someoneAppears.checked
                        color: someoneAppears.down ? "#17a81a" : "#21be2b"
                        radius: 2
                    }
                }
                contentItem: Text {
                    opacity: enabled ? 1.0 : 0.3
                    color: "#ffffff"
                    text: "Someone appears or no one"
                    verticalAlignment: Text.AlignVCenter
                    font: someoneAppears.font
                    leftPadding: someoneAppears.indicator.width + someoneAppears.spacing
                }

                onClicked: {
                    settingsBackend.someoneAppearsClicked(checked)
                    onlyAdmin.checked = false
                    onlyAdminStrict.checked = false
                    someoneAppearsStrict.checked = false
                }

            }


            CheckBox {
                id: autoUnlock
                text: qsTr("CheckBox")
                anchors.left: parent.left
                anchors.top: someoneAppears.bottom
                anchors.leftMargin: 0
                anchors.topMargin: 10
                indicator: Rectangle {
                    x: autoUnlock.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 3
                    border.color: autoUnlock.down ? "#17a81a" : "#21be2b"
                    implicitWidth: 26
                    implicitHeight: 26
                    Rectangle {
                        x: 6
                        y: 6
                        width: 14
                        height: 14
                        visible: autoUnlock.checked
                        color: autoUnlock.down ? "#17a81a" : "#21be2b"
                        radius: 2
                    }
                }
                contentItem: Text {
                    opacity: enabled ? 1.0 : 0.3
                    color: "#ffffff"
                    text: "Auto Unlock"
                    verticalAlignment: Text.AlignVCenter
                    font: autoUnlock.font
                    leftPadding: autoUnlock.indicator.width + autoUnlock.spacing
                }

                onClicked: {
                    settingsBackend.autoUnlockClicked(checked)
                }
            }
        }

        Rectangle {
            id: rightRectangle
            x: 10
            visible: false
            color: "#00000000"
            border.width: 0
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: label.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: parent.width / 2
            anchors.topMargin: 10

            Rectangle {
                id: alignCenter
                y: 0
                width: 384
                height: 200
                color: "#00000000"
                anchors.horizontalCenter: parent.horizontalCenter




                Label {
                    id: labelTime
                    x: 28
                    y: 57
                    color: "#ffffff"
                    text: qsTr("Time Interval")
                    font.pixelSize: 18
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignVCenter
                    font.family: "Times New Roman"
                }
            }

        }

    }

    Connections {
        target: settingsBackend;

        //        function onSetStartup(value) {
        //            autoUnlock.checked = value
        //            print("function", value)
        //        }

    }

    Connections {
        target: backend;

        function onSetAutoUnlock(value) {
            if (value === "true") {
                autoUnlock.checked = true
            }
            else {
                autoUnlock.checked = false
            }
        }

        function onSetOnlyAdminStrict(value) {
            if (value === "true") {
                onlyAdminStrict.checked = true
            }
            else {
                onlyAdminStrict.checked = false
            }
        }

        function onSetOnlyAdmin(value) {
            if (value === "true") {
                onlyAdmin.checked = true
            }
            else {
                onlyAdmin.checked = false
            }
        }

        function onSetSomeoneAppearsStrict(value) {
            if (value === "true") {
                someoneAppearsStrict.checked = true
            }
            else {
                someoneAppearsStrict.checked = false
            }
        }

        function onSetSomeoneAppears(value) {
            if (value === "true") {
                someoneAppears.checked = true
            }
            else {
                someoneAppears.checked = false
            }
        }
    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}D{i:4}D{i:8}D{i:12}D{i:16}D{i:20}
}
##^##*/
