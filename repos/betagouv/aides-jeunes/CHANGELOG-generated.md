## Changelog : aides-jeunes (30 derniers jours)

### Résumé
Ce changelog présente les récentes mises à jour apportées au simulateur d'aides sociales pour les jeunes. Les changements incluent des mises à jour des aides disponibles, des corrections de noms et de liens, l'ajout d'un bouton d'accompagnement après le sondage utilisateur, ainsi que des améliorations techniques pour la CI et le déploiement.

### Évolutions fonctionnelles
- Mise à jour des aides disponibles : les informations sur les aides ont été actualisées. (#5062)
- Suppression de l'aide des Hauts de France pour les étudiants. (#5071)
- Suppression de l'aide au permis de conduire pour les apprentis. (#5069)
- Ajout d'un point de contact pour l'accompagnement par la Maison France Services de Chemillé en Anjou. (#5068)
- Ajout d'un bouton d'accompagnement à la fin du sondage pour orienter les utilisateurs. (#5046)
- Correction du nom "Mes-Aides Jeunes" en "Aides Jeunes" dans les Conditions Générales d'Utilisation (CGU). (#5053)

### Évolutions techniques
- Amélioration de la configuration de la CI pour une meilleure robustesse. (#5048)
- Configuration de la version Node.js pour le déploiement afin d'assurer la compatibilité. (#5054)
- Correction du chemin d'accès pour la génération des statistiques MongoDB, résolvant une erreur signalée par Sentry. (#5066)
- Mise à jour de la dépendance `openfisca-france` dans le répertoire `/openfisca`. (#5063, #5051)
- Mise à jour de la dépendance `next` dans le répertoire `/contribuer`. (#5052)

### Autres changements
- Création de nouvelles entités pour des communautés de communes et des CCAS : Communauté de communes Adour Madiran (#5061) et CCAS de Redon Service Transport Plus Handicap (#5050).
