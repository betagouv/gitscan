## Changelog : aides-jeunes (30 derniers jours)

### Résumé
Ce changelog présente les dernières mises à jour d'Aides Jeunes, le simulateur d'aides sociales pour les jeunes. Les évolutions concernent principalement la mise à jour des informations sur les aides disponibles, l'ajout de nouveaux lieux d'accompagnement et des améliorations techniques pour faciliter la contribution et le déploiement du projet.

### Évolutions fonctionnelles
- Mise à jour des informations sur les aides disponibles (#5062)
- Suppression de l'aide des Hauts de France pour les étudiants (#5071)
- Suppression de l'aide au permis de conduire pour les apprentis (#5069)
- Ajout du rendez-vous d'accompagnement par la Maison France Services de Chemillé en Anjou (#5068)
- Ajout d'un bouton d'accompagnement à la fin du sondage (#5046)
- Ajout de nouveaux lieux d'accompagnement via l'API de data inclusion (#5039)

### Évolutions techniques
- Amélioration de la CI (Continuous Integration) pour des tests plus fiables (#5048)
- Mise à jour de la version de Node.js utilisée pour le déploiement (#5054)
- Correction du chemin d'accès pour la génération des statistiques MongoDB (résolution d'une erreur cron signalée par Sentry) (#5066)
- Mise à jour d'OpenFisca-France (#5049, #5051, #5063)
- Amélioration de la réutilisabilité des thèmes du simulateur (#4966)

### Autres changements
- Correction des références "Mes-Aides Jeunes" vers "Aides Jeunes" dans les CGU (Conditions Générales d'Utilisation) (#5053)
- Création de nouvelles entités (communes, services) via des bots automatisés (#5050, #5061)
- Mise à jour de la dépendance `next` dans le répertoire `/contribuer` (#5052)
