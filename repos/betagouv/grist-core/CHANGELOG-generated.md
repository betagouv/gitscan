## Changelog : grist-core (30 derniers jours)

### Résumé
Les dernières mises à jour de Grist se concentrent sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des problèmes d'affichage et de fonctionnement des suggestions, en améliorant l'intégration avec des fournisseurs d'authentification comme GetGrist.com, et en ajoutant des fonctionnalités d'importation de schémas Airtable. Des efforts importants ont également été consacrés à la traduction de l'interface dans plusieurs langues.

### Évolutions fonctionnelles
- Amélioration de l'affichage des suggestions, notamment pour les références et les listes de références (#2052).
- Correction d'un problème d'affichage et de barre de défilement sur les suggestions sous macOS (#2075).
- Possibilité d'importer des schémas Airtable (#2050).
- Amélioration de l'intégration avec GetGrist.com :
  - Affichage par défaut de l'option "Se connecter avec GetGrist.com" dans le panneau d'administration (#2077).
  - Ajout de notifications par email pour les suggestions (#2071).
  - Gestion des sessions lors du changement de fournisseur d'authentification (#2071).
  - Ajout des nouveaux utilisateurs GetGrist.com à SendGrid (#2064).
- Correction d'un bug empêchant l'affichage correct des suggestions sur les documents avec des tables supprimées (#2069).
- Amélioration de la gestion des noms longs pour les aperçus, limités à 63 caractères (#2077).
- Correction d'un bug lié à l'affichage des rôles dans l'API SCIM (#2051).
- Ajout de préférences pour activer l'installation de l'administrateur au redémarrage.

### Évolutions techniques
- Mise à jour de la bibliothèque Lodash de la version 4.17.21 à la version 4.17.23 (#2062).
- Refactorisation et déplacement de tests pour le bac à sable (sandbox) vers `grist-core` (#2073, #2088, #2095).
- Optimisation du chargement des fichiers de documentation (#2083, #2084).
- Mise à jour de la version de `grist-ee` (#2084).
- Correction d'un problème lié à une règle ESLint (brace-style) (#2087).
- Amélioration de la gestion des chemins d'accès pour l'importation de fichiers dans le bac à sable (#2064).

### Autres changements
- Ajout et mise à jour de traductions dans plusieurs langues : Hongrois, Suédois, Français, Indonésien, Basque, Polonais, Anglais (Royaume-Uni) (#2096, #2095, #2085, #2067 et autres).
- Signature de la CLA (Contributor License Agreement) par plusieurs contributeurs (#2096, #2085).
- Mise à jour des fichiers de traduction via Weblate.
