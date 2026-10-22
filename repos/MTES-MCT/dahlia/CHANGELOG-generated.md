## Changelog : dahlia (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une refonte de l'interface de gestion des dossiers pour faciliter la saisie et la lecture des informations grâce à de nouveaux blocs de données et une meilleure organisation visuelle. Parallèlement, la sécurité et la fiabilité du système ont été renforcées par l'ajout de journaux d'audit, une meilleure gestion des erreurs et une optimisation des échanges avec les services externes (Télérecours).

### Évolutions fonctionnelles
- **Amélioration de l'interface de gestion des dossiers** : réorganisation des onglets, ajout de nouveaux blocs (informations, qualification, commentaires) et mise en évidence visuelle (en rouge) des champs nécessitant une validation ([#195](https://github.com/MTES-MCT/dahlia/pull/195), [#196](https://github.com/MTES-MCT/dahlia/pull/196), [#197](https://github.com/MTES-MCT/dahlia/pull/197), [#198](https://github.com/MTES-MCT/dahlia/pull/198), [#202](https://github.com/MTES-MCT/dahlia/pull/202)).
- **Évolution des fonctionnalités métier** : intégration de nouvelles règles de classification ([#170](https://github.com/MTES-MCT/dahlia/pull/170), [#194](https://github.com/MTES-MCT/dahlia/pull/194), [#156](https://github.com/MTES-MCT/dahlia/pull/156)), ajout d'un bouton pour le formulaire de retour utilisateur ([#180](https://github.com/MTES-MCT/dahlia/pull/180)) et inclusion du statut dans les exports de classification ([#153](https://github.com/MTES-MCT/dahlia/pull/153)).
- **Gestion des juridictions** : possibilité de synchroniser l'intégralité des dossiers pour le département 69 ([#159](https://github.com/MTES-MCT/dahlia/pull/159)).
- **Accessibilité et légal** : mise à disposition des pages de mentions légales pour l'ensemble des utilisateurs ([#155](https://github.com/MTES-MCT/dahlia/pull/155), [#151](https://github.com/MTES-MCT/dahlia/pull/151)).

### Évolutions techniques
- **Sécurité et traçabilité** : mise en place de logs d'audit pour les refus d'accès ([#174](https://github.com/MTES-MCT/dahlia/pull/174)) et les actions administratives ([#158](https://github.com/MTES-MCT/dahlia/pull/158)), renforcement du contrôle de validité des sessions ([#171](https://github.com/MTES-MCT/dahlia/pull/171)) et masquage des erreurs techniques sensibles pour l'utilisateur final ([#157](https://github.com/MTES-MCT/dahlia/pull/157), [#173](https://github.com/MTES-MCT/dahlia/pull/173)).
- **Optimisation et robustesse** : passage de la synchronisation des dossiers en mode asynchrone ([#152](https://github.com/MTES-MCT/dahlia/pull/152)), ajout d'un limiteur de débit (rate limiting) pour les appels à l'API Télérecours ([#187](https://github.com/MTES-MCT/dahlia/pull/187)) et automatisation de la synchronisation (cron) pour le département 93 ([#188](https://github.com/MTES-MCT/dahlia/pull/188)).
- **Architecture et données** : modification de la structure des clés primaires pour inclure le code de juridiction ([#175](https://github.com/MTES-MCT/dahlia/pull/175)), isolation des instances de données pour certaines juridictions ([#160](https://github.com/MTES-MCT/dahlia/pull/160)) et correction de la logique de suppression des dossiers pour garantir l'étanchéité entre les juridictions ([#161](https://github.com/MTES-MCT/dahlia/pull/161)).
- **Authentification** : amélioration du processus de déconnexion avec redirection automatique vers ProConnect ([#169](https://github.com/MTES-MCT/dahlia/pull/169)).

### Autres changements
- Mise à jour de plusieurs librairies pour corriger des vulnérabilités de sécurité ([#167](https://github.com/MTES-MCT/dahlia/pull/167), [#166](https://github.com/MTES-MCT/dahlia/pull/166)).
