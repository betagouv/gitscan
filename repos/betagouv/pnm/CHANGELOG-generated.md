## Changelog : pnm (30 derniers jours, au 16 octobre 2026)

### Résumé
Le projet est passé d'une structure de base à une application fonctionnelle. Les utilisateurs peuvent désormais naviguer via un parcours guidé en trois étapes, sélectionner un parc naturel marin et visualiser la localisation de leur projet sur une carte interactive. Les données officielles de l'OFB sont désormais intégrées pour alimenter l'application.

### Évolutions fonctionnelles
- **Parcours utilisateur** : Mise en place d'un guide en trois étapes pour accompagner les porteurs de projet [#4](https://github.com/betagouv/pnm/pull/4).
- **Navigation et sélection** : Création de la page d'accueil, du système de routage et de la sélection des parcs [#3](https://github.com/betagouv/pnm/pull/3).
- **Cartographie** : Ajout d'une fonctionnalité de dessin et de visualisation de la localisation du projet sur une carte [#5](https://github.com/betagouv/pnm/pull/5).
- **Données officielles** : Intégration des données de l'OFB pour les périmètres des parcs, la liste des activités et la liste des parcs.
- **Interface utilisateur** : 
    - Intégration du Design System de l'État (DSFR).
    - Ajout de l'identité visuelle de l'OFB (logo) dans le header et le footer.
    - Correction du défilement automatique en haut de page lors de la navigation.

### Évolutions techniques
- **Architecture** : Unification du serveur pour servir l'API et le front-end via un processus unique.
- **API** : Implémentation d'un routeur avec un endpoint de santé (*health check*) et gestion des données via des fichiers validés.
- **CI/CD** : Mise en place de workflows GitHub Actions et automatisation du déploiement sur Scalingo [#2](https://github.com/betagouv/pnm/pull/2).
- **Développement** : 
    - Configuration de TypeScript et des *npm workspaces*.
    - Optimisation du code via la création de helpers partagés pour les appels API et la mutualisation des types de données.

### Autres changements
- **Documentation** : Rédaction de la documentation technique (organisation du code, commandes, déploiement) et fonctionnelle (description des étapes du parcours et choix de la cartographie).
