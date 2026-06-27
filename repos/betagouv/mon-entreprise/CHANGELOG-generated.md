## Changelog : mon-entreprise (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec une refonte du comparateur de statuts, l'ajout de fonctionnalités spécifiques pour Mayotte et une amélioration de l'accessibilité. Des efforts importants ont également été réalisés sur l'infrastructure technique pour préparer le passage à Next.js et améliorer la performance et la robustesse de l'application.

### Évolutions fonctionnelles

*   **Comparateur de statuts :** Nouvelle mise en page du comparateur, regroupement des questions, ajout de la navigation entre les questions principales et la situation complète, et ajout d'un bouton pour restaurer les valeurs par défaut.
*   **Mayotte :** Ajout de cotisations spécifiques à Mayotte, affichage d'avertissements spécifiques, et masquage des points de retraite complémentaire pour les A/C/PLNR mahorais. Correction du revenu cotisé pour la retraite de base.
*   **Cessation d'activité :** Ajout d'un message d'erreur en cas de date de cessation invalide, correction de la réinitialisation de la date de cessation, et affichage d'un avertissement en cas de changement d'année.
*   **Artiste-auteur :** Mise à jour de la description et du guide IRCEC.
*   **Avertissements :** Amélioration de l'avertissement pour les outils en version bêta et pour les auto-entrepreneureuses.
*   **Messages :** Possibilité de dismisser les messages d'information.
*   **Smic :** Mise à jour du montant du SMIC.

### Évolutions techniques

*   **Next.js :** Préparation du passage à Next.js avec des refactorings importants :
    *   Configuration de la langue par défaut côté serveur.
    *   Amélioration de la gestion du DarkMode avec persistance via cookies.
    *   Utilisation de `next/font/local` pour le chargement des fonts.
    *   Optimisation du chargement des styles et des scripts.
*   **Design System :** Refactorings pour améliorer la cohérence et la maintenabilité du design system.
*   **Tests :** Ajout de tests unitaires pour certaines fonctionnalités.
*   **Infrastructure :** Ajout de Scalingo au devShell Nix.
*   **API :** Amélioration de la gestion des erreurs Redis et remontée de l'indisponibilité de Redis à Sentry.
*   **Typage :** Amélioration du typage TypeScript.
*   **Suppression de dépendances :** Suppression de dépendances inutiles.

### Autres changements

*   **Documentation :** Mise à jour du lien vers le site QPV.
*   **Linting :** Corrections de linting.
*   **Base de données :** Mise à jour des données de base (base-stats.json).
*   **Traduction :** Corrections de traductions.
*   **Accessibilité :** Améliorations de l'accessibilité (ajout de rôles ARIA, amélioration des contrastes, etc.).
