## Changelog : etape (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience utilisateur grâce à l'adoption d'un nouveau design system et une refonte complète du simulateur (questions et affichage des résultats). Parallèlement, la plateforme a gagné en fiabilité et en sécurité avec une gestion plus intelligente des sessions (avertissements avant déconnexion) et une modernisation profonde de l'infrastructure technique (migration vers pnpm et Vite).

### Évolutions fonctionnelles
- **Refonte du simulateur** : 
    - Nouveau design des questions (1 à 7) et des cartes de choix.
    - Amélioration de la page de résultats : mise en avant du résultat prioritaire, nouvelle mise en page des cartes et ajout d'une phrase récapitulative.
    - Optimisation de l'export PDF (mise en page et typographie).
- **Nouvelle identité visuelle** : 
    - Intégration du nouveau design system (couleurs, typographies Geist/Bricolage Grotesque, rayons, et composants comme les Tooltips).
    - Mise à jour de la barre de marque avec le logo Transitions Pro.
    - Création de nouveaux composants d'interface : `TopBar` et `DossierHeader` [#186](https://github.com/betagouv/etape/issues/186).
- **Gestion de la session** : 
    - Mise en place d'un système d'alerte avant la fin de session avec possibilité de prolongation automatique tant que l'utilisateur est actif [#73](https://github.com/betagouv/etape/issues/73).
- **Accessibilité et ergonomie** : 
    - Annonce de l'enregistrement automatique pour les lecteurs d'écran.
    - Amélioration de la lisibilité des libellés et des textes secondaires sur les fonds colorés.
    - Ajout du numéro de dossier dans le glossaire.

### Évolutions techniques
- **Modernisation de la stack** : 
    - Migration complète du monorepo de `npm` vers `pnpm` [#90](https://github.com/betagouv/etape/issues/90).
    - Migration du front-office et du back-office vers `Vite` [#71](https://github.com/betagouv/etape/issues/71).
    - Adoption de `TanStack Router` pour la gestion de la navigation.
- **Sécurité renforcée** : 
    - Protection des inscriptions et des procédures de mot de passe oublié via ALTCHA [#79](https://github.com/betagouv/etape/issues/79).
    - Ajout de protections CSRF sur les requêtes de modification de données.
    - Amélioration de la gestion des cookies (préfixage `__Host-` en production) et isolation des sessions par application.
- **Architecture et performance** : 
    - Centralisation de la logique de session dans un package dédié (`packages/session`).
    - Optimisation des performances front-end (poids du bundle et rendus).
    - Extraction de la logique métier (avancement du dossier) vers la couche `domain/`.

### Autres changements
- **Documentation** : Mise à jour des guides d'installation, de la cartographie des applications [#74](https://github.com/betagouv/etape/issues/74) et des consignes d'authentification.
- **Expérience développeur** : Ajout de la commande `npm run dev:stack` pour simplifier le lancement de l'environnement de développement local.
