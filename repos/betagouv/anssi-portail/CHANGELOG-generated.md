## Changelog : anssi-portail (30 derniers jours, au 12 août 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience utilisateur, tant sur le plan visuel que fonctionnel. Le portail adopte une nouvelle identité graphique et déploie les "parcours de sécurisation", permettant aux organisations de suivre leur progression et d'obtenir des attestations officielles (badges et documents PDF).

### Évolutions fonctionnelles
- **Parcours de sécurisation** : 
    - Mise en place des parcours "Basique" et "Complet" avec un suivi de progression détaillé (barres de progression, badges de complétion).
    - Nouveau système de récompenses permettant de télécharger des archives ZIP contenant des attestations PDF personnalisées et des badges (notamment le badge Cyberdépart).
    - Gestion des modules de formation avec affichage des mesures et tutoriels intégrés.
- **Refonte visuelle (Nouvelle DA)** : 
    - Déploiement d'une nouvelle charte graphique incluant de nouveaux composants "Héros", une nouvelle palette de couleurs et des illustrations mises à jour.
    - Amélioration de l'ergonomie sur mobile et tablette pour l'ensemble des sections clés.
- **Améliorations thématiques** :
    - Mise à jour de la section NIS 2 et de son simulateur.
    - Optimisation de la section "Guides et Ressources" et des statistiques.
- **Expérience utilisateur** : 
    - Amélioration du wording (textes) sur l'ensemble du portail pour plus de clarté.
    - Ajout d'un système de consentement pour le suivi (pixel) et de notifications (toasters) plus explicites.

### Évolutions techniques
- **Performance et SEO** : 
    - Généralisation du rendu côté serveur (SSR) pour de nombreuses pages (Guides, Statistiques, NIS 2, Accueil, etc.) afin d'optimiser le temps de chargement et le référencement.
- **Architecture et composants** :
    - Migration et mise à jour vers Svelte 5.
    - Standardisation massive des composants via l'utilisation du Design System de l'État (DSFR).
    - Refonte de la bibliothèque de composants interne (UI-Kit).
- **Sécurité et DevOps** :
    - Renforcement de la sécurité de la CI avec l'ajout de scans antivirus.
    - Amélioration de la gestion des secrets et masquage des variables d'environnement.
    - Sécurisation des mécanismes de redirection d'URL côté serveur.
- **Qualité logicielle** :
    - Renforcement de la couverture de tests (Vitest, Playwright) et introduction de tests de snapshot pour garantir la stabilité visuelle.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement et des procédures d'exploitation.
- **Maintenance** : Nettoyage de l'application avec la suppression de pages obsolètes (anciennes pages "promouvoir") et de code non utilisé.
