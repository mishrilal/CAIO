import QtQuick 2.15
import QtQuick.Shapes 1.15
import QtGraphicalEffects 1.15

Item {
    id: progress
    implicitWidth: 250
    implicitHeight: 250

    // Properties
    // General
    property bool roundCap: true
    property int startAngle: 90
    property real maxValue: 100
    property real value: 55
    property int samples: 12
    // Drop Shadow
    property bool enableDropShadow: false
    property color dropShadowColor: "#20000000"
    property int dropShadowRadius: 10
    // Bg Circle
    property color bgColor: "transparent"
    property color bgStrokeColor: "#7e7e7e"
    property int strokeBgWidth: 16
    // Progress Circle
    property color progressColor: "#1842d1"
    property int progressWidth: 16
    // Text
    property string text: ""
    property bool textShowValue: true
    property string textFontFamily: "Times New Roman"
    property int textSize: 12
    property color textColor: "#ffffff"
    property string infoText: "Count"

    // Internal Properties/Functions
    QtObject{
        id: internal

        property Component dropShadow: DropShadow{
            color: progress.dropShadowColor
            fast: true
            verticalOffset: 0
            horizontalOffset: 0
            samples: progress.samples
            radius: progress.dropShadowRadius
        }
    }


    Shape{
        id: shape
        anchors.fill: parent
        layer.enabled: true
        layer.samples: progress.samples
        layer.effect: progress.enableDropShadow ? internal.dropShadow : null

        Text {
            id: textProgress
            text: progress.textShowValue ? parseInt(progress.value) + progress.text : progress.text
            anchors.verticalCenter: parent.verticalCenter
            font.family: "Times New Roman"
            font.pointSize: 22
            anchors.verticalCenterOffset: -20
            anchors.horizontalCenter: parent.horizontalCenter
            color: progress.textColor
        }

        ShapePath{
            id: pathBG
            strokeColor: progress.bgStrokeColor
            fillColor: progress.bgColor
            strokeWidth: progress.strokeBgWidth
            capStyle: progress.roundCap ? ShapePath.RoundCap : ShapePath.FlatCap

            PathAngleArc{
                radiusX: (progress.width / 2) - (progress.progressWidth / 2)
                radiusY: (progress.height / 2) - (progress.progressWidth / 2)
                centerX: progress.width / 2
                centerY: progress.height / 2
                startAngle: progress.startAngle
                sweepAngle: 360
            }
        }

        Text {
            id: infoText
            width: parent.width - 30
            color: "#7c7c7c"
            text: progress.infoText
            anchors.top: textProgress.bottom
            font.pixelSize: 16
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignTop
            wrapMode: Text.WordWrap
            padding: 4
            anchors.horizontalCenterOffset: 0
            anchors.topMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
            font.family: "Times New Roman"
        }

        ShapePath{
            id: path
            strokeColor: progress.progressColor
            fillColor: "transparent"
            strokeWidth: progress.progressWidth
            capStyle: progress.roundCap ? ShapePath.RoundCap : ShapePath.FlatCap

            PathAngleArc{
                radiusX: (progress.width / 2) - (progress.progressWidth / 2)
                radiusY: (progress.height / 2) - (progress.progressWidth / 2)
                centerX: progress.width / 2
                centerY: progress.height / 2
                startAngle: progress.startAngle
                sweepAngle: (360 / progress.maxValue * progress.value)
            }
        }


    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:2;height:250;width:250}
}
##^##*/
