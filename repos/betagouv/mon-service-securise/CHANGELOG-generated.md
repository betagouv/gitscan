## Changelog : mon-service-securise (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'interface utilisateur avec l'intégration du Design System de la République Française (DSFR), l'amélioration de la gestion des risques (notamment avec l'introduction des risques spécifiques v2) et l'ajout de la page Indice Cyber. De nombreuses corrections et optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Intégration du header DSFR, remplaçant l'ancien header custom.
- Ajout du composant de page "Indice Cyber" avec affichage du radar et des tranches d'indice.
- Ajout de la navigation horizontale dans la section "SÉCURISER".
- Ajout de la gestion des risques spécifiques v2 : création, modification, suppression et affichage dans l'interface.
- Possibilité d'exporter les risques V1 au format CSV.
- Ajout d'une modale pour afficher les cartographies de risques.
- Ajout d'un tiroir pour l'ajout de risque spécifique v2.
- Affichage du nom du service dans l'en-tête des pages de service.
- Ajout du bouton de gestion des contributeurs.
- Amélioration de l'affichage des informations de service dans la page "Décrire".
- Ajout d'une route pour marquer comme "vu" les explications des risques V2.

### Évolutions techniques
- Migration de la page "Mesures" et "Décrire V2" vers une application SPA (Single Page Application).
- Refonte de la navigation principale avec le composant `dsfr-navigation`.
- Utilisation des slots du header DSFR pour une meilleure personnalisation.
- Suppression de l'ancien code Pug au profit de Svelte.
- Amélioration de la gestion des données et des objets de données pour les risques v2.
- Refactorisation du code pour une meilleure organisation et maintenabilité.
- Mise à jour de nombreuses dépendances (Svelte, Vite, TypeScript, ESLint, etc.).
- Ajout de tests d'accessibilité avec Playwright et Axe.
- Configuration de l'exécution des tests d'accessibilité en CI/CD.
- Amélioration de la gestion des feature flags.

### Autres changements
- Suppression du bandeau de promotion de MSC.
- Correction de problèmes d'accessibilité.
- Amélioration de la documentation et des commentaires.
- Nettoyage du code et suppression de code obsolète.
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Mise à jour des variables d'environnement pour les tests d'accessibilité.
- Ajout de rapports d'exécution des tests d'accessibilité.
- Correction de la bordure du menu de page service.
- Harmonisation de l'identifiant de la page `contactsUtiles`.
- Correction de l'affichage des valeurs d'indice cyber.
- Suppression des fichiers d'en-tête inutiles.
- Suppression des anciennes vues `pug`.
- Correction des retours du pôle Design sur la page Indice Cyber.
- Ajout des données concernant les indices cyber dans l'objet d'API service complet.
- Correction d'erreurs liées aux routes et à la gestion des paramètres de requête.
- Suppression de code obsolète et de styles inutilisés.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
