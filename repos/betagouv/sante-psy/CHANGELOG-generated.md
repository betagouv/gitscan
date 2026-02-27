## Changelog : sante-psy (30 derniers jours)

### Résumé
Ce mois-ci, l'application Santé Psy Étudiant a bénéficié d'améliorations significatives, notamment le développement de l'espace étudiant et des corrections concernant la gestion des psychologues inactifs dans l'annuaire. Des optimisations ont également été apportées à la recherche de psychologues via la géolocalisation.

### Évolutions fonctionnelles
- **Espace étudiant :** Un espace dédié aux étudiants a été implémenté (#780).
- **Annuaire des psychologues :** Les profils de psychologues inactifs ne sont plus affichés dans l'annuaire public (#800, #936bbbe).
- **Connexion psychologue :** Correction d'un bug empêchant la connexion des psychologues inactifs sans raison de suspension (#95c5de1).
- **Géolocalisation :** La recherche de psychologues utilise désormais une source de données géographiques plus fiable et à jour (#789).
- **FAQ et CGU :** Mise à jour des textes de la FAQ et des Conditions Générales d'Utilisation (#811).

### Évolutions techniques
- **Optimisation des requêtes :** Amélioration de la performance de la requête comptant les rendez-vous (#812).
- **Linting :** Application de règles de linting pour améliorer la qualité du code (#d396bd0).

### Autres changements
- Correction d'un test supprimé par erreur (#f2456db).
- Application de la convention de nommage pour forcer la casse en majuscules (#b68a68b).
