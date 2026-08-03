## Changelog : rdv-insertion (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette version apporte des améliorations de performance, notamment sur l'index des utilisateurs, et corrige des bugs liés à l'expiration des invitations, à l'affichage des filtres et à la gestion des orientations post-RDV. La documentation du schéma de données a également été mise à jour.

### Évolutions fonctionnelles
- Correction du formatage des instructions de rendez-vous dans les lettres de convocation [#3349](https://github.com/gip-inclusion/rdv-insertion/issues/3349).
- Amélioration du contenu de l'infobulle de disponibilité des créneaux pour les utilisateurs [#3339](https://github.com/gip-inclusion/rdv-insertion/issues/3339).
- Ajout de nouveaux filtres à l'index des utilisateurs [#3338](https://github.com/gip-inclusion/rdv-insertion/issues/3338).
- Possibilité de rouvrir un suivi une fois celui-ci fermé [#3340](https://github.com/gip-inclusion/rdv-insertion/issues/3340).
- Suppression du formulaire de comptage des orientations post-RDV [#3341](https://github.com/gip-inclusion/rdv-insertion/issues/3341).
- Correction d'un bug empêchant la suppression correcte du filtre lors de clics répétés sur le bouton de raccourci [#3344](https://github.com/gip-inclusion/rdv-insertion/issues/3344).
- Mise à jour de la documentation du schéma de données avec l'origine des données [#3342](https://github.com/gip-inclusion/rdv-insertion/issues/3342).

### Évolutions techniques
- Amélioration de la performance de l'endpoint d'indexation des utilisateurs [#3358](https://github.com/gip-inclusion/rdv-insertion/issues/3358).
- L'expiration des invitations est désormais gérée de manière asynchrone [#3357](https://github.com/gip-inclusion/rdv-insertion/issues/3357).
- Augmentation du délai d'attente pour la migration des origines d'invitation [#3343](https://github.com/gip-inclusion/rdv-insertion/issues/3343).
- Application de l'index en dernier lors de la migration et augmentation du délai d'attente.
- Mise à jour de plusieurs dépendances : `rails-html-sanitizer`, `js-yaml`, `brace-expansion`, `actions/setup-node`, `websocket-driver`, `css_parser`.

### Autres changements
- Mise à jour de la déclaration d'accessibilité dans la vue [#3355](https://github.com/gip-inclusion/rdv-insertion/issues/3355).
- Mise à jour des dépendances suite à un scan de sécurité [#3354](https://github.com/gip-inclusion/rdv-insertion/issues/3354).
