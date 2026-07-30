## Changelog : referentiel-applications (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment au niveau de la gestion des applications, des filtres et de la matrice des droits. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des améliorations d'accessibilité (RGAA). Des travaux ont également été réalisés sur la gestion des permissions et la performance de la recherche.

### Évolutions fonctionnelles
- Ajout de la possibilité de gérer plusieurs divisions métiers.
- Amélioration de la recherche globale avec préfixe et correction de sa fiabilité.
- Affichage du libellé de statut même sans date sur les applications.
- Ajout de l'option de tri des types d'acteur.
- Amélioration de l'interface pour la création d'applications (étapes, labels).
- Ajout de la gestion des licences et de la stack technique sur la fiche d'application.
- Amélioration de l'interface de filtrage côté application avec ajout d'un espacement entre le portefeuille et les informations générales.
- Mise à jour de l'affichage de la version de l'application sans rafraîchissement complet de la page.
- Mise à jour du nom de "time" pour "mco".
- Ajout de la possibilité de définir une date de statut optionnelle.
- Ajout de la gestion des importations MOA/MOE avec l'indicateur "is group".
- Correction du calcul de la valeur totale pour le MDIT.

### Évolutions techniques
- Refonte de la stack technologique affichée sur la fiche application (produit, lien documentation, fin de vie).
- Amélioration de la performance de la recherche d'applications.
- Fiabilisation du démarrage de la base de données et du backend en CI pour éviter les tests aléatoires.
- Correction d'un problème de pollution de la base de données de développement par les tests.
- Suppression de la fonctionnalité de gestion des licences (modèle, API, UI, tests).
- Correction de plusieurs alertes de sécurité (Dependabot) sur le frontend et le backend.
- Amélioration de la gestion des permissions : suppression du mécanisme `isAdmin` et simplification des droits.
- Ajout d'un endpoint pour le catalogue de données et actions associées en frontend.
- Ajout de permissions d'écriture pour l'édition des données d'application.

### Autres changements
- Améliorations de l'accessibilité (RGAA) : contraste des couleurs, champs de formulaires, messages de statut, accessibilité des graphiques, gestion du focus clavier, etc.
- Ajout de documentation récapitulative du RefApp et des ADR (Architectural Decision Records).
- Correction d'un bug empêchant l'édition d'une ligne de matrice non verrouillée.
- Amélioration de la gestion des filtres dans l'interface d'administration.
- Mise à jour des dépendances (versions 1.82.0, 1.82.1, 1.83.0, 1.84.0, 1.85.0 et 1.86.0).
- Ajout de tests E2E pour améliorer la couverture et la fiabilité.
- Correction de problèmes de localisation de certains éléments de l'interface utilisateur.
- Ajout de la validation par défaut dans les filtres d'application.
- Amélioration de la gestion des erreurs et des messages d'information.
- Ajout de la gestion des tokens applicatifs admin pour FP8.
