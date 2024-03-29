import QtQuick 2.15
//import QtQuick.Controls 1.4 as OldControls
//import QtQuick.Controls 1.4
import QtQuick.Controls 2.15
import Qt.labs.qmlmodels 1.0
import QtQuick.Layouts 1.0
import QtGraphicalEffects 1.15
import QtQuick.Timeline 1.0

import "../controls/"

Item {
    id: item1
    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent

        Label {
            id: label
            visible: false
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
            anchors.topMargin: 10

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
                            opacity: 0
                            value: 0
                            startAngle: 90
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
                        anchors.rightMargin: 10
                        anchors.leftMargin: 10
                        CircularProgress {
                            id: circularProgressCenter
                            text: " "
                            anchors.fill: parent
                            value: 0.01
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
//                            opacity: 0
//                            value: 0
//                            startAngle: 90
//                            progressColor: "#bfdd04"
//                            progressWidth: 6
//                            textSize: 14
//                            roundCap: false
//                            strokeBgWidth: 6
//                            bgStrokeColor: "#101010"
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
                    anchors.bottomMargin: 10
                    clip: true
                    anchors.topMargin: 10

                    ScrollView {
                        id: scrollView
                        anchors.fill: parent
                        anchors.bottomMargin: 0

                        TableView {
                                id: tableView
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

        function onSetMaxValue(value) {
            circularProgressLeft.maxValue = value
            circularProgressCenter.maxValue = value
            circularProgressRight.maxValue = value
            cicrularProgressLeftKeyFrameMaxValue.value = value
            cicrularProgressCenterKeyFrameMaxValue.value = value
            cicrularProgressRightKeyFrameMaxValue.value = value
//            print("Total Locks", value)
        }

        function onSetAdminLocks(value) {
            circularProgressLeft.value = value
            cicrularProgressLeftKeyFrameValue.value = value
        }

        function onSetSomeoneElseLocks(value) {
            circularProgressCenter.value = value
            cicrularProgressCenterKeyFrameValue.value = value
        }

        function onSetNobodyLocks(value) {
            circularProgressRight.value = value
            cicrularProgressRightKeyFrameValue.value = value
        }
    }


    Timeline {
        id: timeline
        animations: [
            TimelineAnimation {
                id: timelineAnimation
                running: true
                loops: 1
                duration: 3000
                to: 3000
                from: 0
            }
        ]
        endFrame: 3000
        enabled: true
        startFrame: 0

        KeyframeGroup {
            target: circularProgressLeft
            property: "opacity"
            Keyframe {
                frame: 800
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: circularProgressCenter
            property: "opacity"
            Keyframe {
                frame: 800
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }

        KeyframeGroup {
            target: circularProgressRight
            property: "opacity"
            Keyframe {
                frame: 800
                value: 1
            }

            Keyframe {
                frame: 0
                value: 0
            }
        }


        KeyframeGroup {
            target: circularProgressLeft
            property: "value"
            Keyframe {
                id: cicrularProgressLeftKeyFrameMaxValue
                easing.bezierCurve: [0.664,0.0036,0.334,1,1,1]
                frame: 1100
                value: 100
            }

            Keyframe {
                frame: 0
                value: 0
            }

            Keyframe {
                id: cicrularProgressLeftKeyFrameValue
                frame: 1600
                value: 0
            }
        }

        KeyframeGroup {
            target: circularProgressCenter
            property: "value"
            Keyframe {
                id: cicrularProgressCenterKeyFrameMaxValue
                easing.bezierCurve: [0.664,0.0036,0.334,1,1,1]
                frame: 1100
                value: 100
            }

            Keyframe {
                frame: 0
                value: 0
            }

            Keyframe {
                id: cicrularProgressCenterKeyFrameValue
                frame: 1600
                value: 0
            }
        }

        KeyframeGroup {
            target: circularProgressRight
            property: "value"
            Keyframe {
                id: cicrularProgressRightKeyFrameMaxValue
                easing.bezierCurve: [0.664,0.0036,0.334,1,1,1]
                frame: 1100
                value: 100
            }

            Keyframe {
                frame: 0
                value: 0
            }

            Keyframe {
                id: cicrularProgressRightKeyFrameValue
                frame: 1600
                value: 0
            }
        }


    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:22}
}
##^##*/
