## Changelog : sante-psy (30 derniers jours)

### Résumé
Ce mois-ci, l'application Santé Psy Étudiant a bénéficié d'améliorations significatives, notamment l'ajout d'un espace dédié aux étudiants et des corrections concernant la visibilité des psychologues inactifs dans l'annuaire. De plus, la géolocalisation a été mise à jour pour utiliser une source de données plus fiable.

### Évolutions fonctionnelles
- **Espace étudiant :** Un nouvel espace a été créé pour les étudiants, améliorant leur expérience et leur permettant d'accéder à des fonctionnalités dédiées. (#780)
- **Annuaire des psychologues :** Les profils des psychologues inactifs ne sont plus affichés dans l'annuaire public. (#800, #936bbbe)
- **Connexion des psychologues :** Correction d'un bug empêchant la connexion des psychologues inactifs sans raison de suspension. (#95c5de1)
- **FAQ et CGU :** Mise à jour du contenu de la FAQ et des Conditions Générales d'Utilisation pour plus de clarté. (#811)

### Évolutions techniques
- **Géolocalisation :** L'API de géolocalisation a été mise à jour pour utiliser les données GeoPF, remplaçant une API obsolète. (#789)
- **Linting :** Application du linting pour améliorer la qualité du code. (d396bd0)

### Autres changements
- Correction d'une erreur dans les tests suite à une suppression accidentelle. (f2456db)
- Force uppercase pour une cohérence interne. (b68a68b)
