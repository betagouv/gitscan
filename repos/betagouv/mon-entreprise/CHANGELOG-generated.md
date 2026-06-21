## Changelog : mon-entreprise (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du comparateur de statuts et des simulateurs, avec une nouvelle mise en page et des fonctionnalités de navigation améliorées. Des corrections importantes ont également été apportées au calcul des cotisations sociales, en particulier pour les cas spécifiques de Mayotte et des régimes Sasu. Enfin, des optimisations techniques ont été réalisées pour préparer le site à une migration vers Next.js et améliorer sa performance.

### Évolutions fonctionnelles
- **Comparateur de statuts :** Nouvelle mise en page pour une meilleure lisibilité et navigation entre les questions principales et la situation complète. Ajout d'un bouton "valeurs par défaut". Amélioration de l'accessibilité avec des liens pour sauter à la partie détails.
- **Simulateurs :** Amélioration de l'affichage des objectifs avec des tooltips d'aide. Suppression de la distinction entre réponses de l'utilisateur et valeurs par défaut.
- **Fiche de paie (SASU) :** Ajout d'une fiche de paie pour le régime SASU, incluant le calcul des cotisations et la présentation des différents éléments de rémunération.
- **Mayotte :** Mise à jour des règles de calcul des cotisations pour tenir compte des spécificités de Mayotte, notamment pour les cotisations maladie, allocations familiales et la participation de la CPAM.
- **Artiste-auteur :** Modifications et mises à jour des informations relatives à l'IRCEC.
- **Cessation d'activité :** Ajout d'un message d'erreur en cas de date de cessation trop ancienne et amélioration de la gestion de la date de cessation.
- **Messages :** Les messages sont désormais dismissibles.
- **Avertissements :** Ajout d'un avertissement spécifique pour Mayotte.

### Évolutions techniques
- **Next.js :** Préparation du site pour une migration vers Next.js avec des améliorations de la configuration, de la gestion des cookies et de la persistance du thème.
- **TypeScript :** Renommage de fichiers et de fonctions pour une meilleure cohérence et pour éviter des erreurs liées à des caractères non-ASCII.
- **Design System :** Utilisation des composants du design system dans la page d'accueil pour valider le thème.
- **Tests :** Ajout de tests unitaires pour les hooks et correction de tests existants.
- **Performance :** Optimisation du chargement des fonts avec `next/font/local` et utilisation de CSS variables.
- **Refactoring :** Refactorisation de plusieurs composants et fichiers pour une meilleure organisation et maintenabilité du code. Suppression de code inutile et simplification de la logique.
- **i18n :** Amélioration de la gestion de l'internationalisation et correction de clés de traduction.

### Autres changements
- Mise à jour du Smic.
- Mise à jour des données de base statistiques.
- Corrections de typos et améliorations de la documentation.
- Amélioration des couleurs et du contraste de certains composants.
- Ajout d'icônes et amélioration de l'accessibilité.
- Mise à jour des dépendances (React, Storybook, recharts).
