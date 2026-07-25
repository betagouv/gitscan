## Changelog : rdv-insertion (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières mises à jour de rdv-insertion se concentrent sur l'amélioration des performances, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter le suivi des parcours d'accompagnement social et professionnel. Des améliorations ont été apportées à la gestion des invitations, à l'affichage des utilisateurs et à la gestion des suivis.

### Évolutions fonctionnelles
- Amélioration du formatage des instructions de rendez-vous dans les lettres de convocation. [#3349](https://github.com/gip-inclusion/rdv-insertion/issues/3349)
- Ajout de filtres à l'index des utilisateurs pour une recherche plus efficace. [#3338](https://github.com/gip-inclusion/rdv-insertion/issues/3338)
- Possibilité de rouvrir un suivi une fois celui-ci fermé. [#3340](https://github.com/gip-inclusion/rdv-insertion/issues/3340)
- Amélioration du contenu de l'infobulle de disponibilité des créneaux pour les utilisateurs. [#3339](https://github.com/gip-inclusion/rdv-insertion/issues/3339)
- Suivi de l'agent qui envoie les invitations. [#3317](https://github.com/gip-inclusion/rdv-insertion/issues/3317)
- Création du suivi même en l'absence de numéro de téléphone ou d'adresse e-mail de l'utilisateur. [#3329](https://github.com/gip-inclusion/rdv-insertion/issues/3329)
- Suppression du formulaire de bilan post-rendez-vous. [#3341](https://github.com/gip-inclusion/rdv-insertion/issues/3341)
- Amélioration de l'accessibilité avec une mise à jour de la déclaration d'accessibilité. [#3355](https://github.com/gip-inclusion/rdv-insertion/issues/3355)
- Correction d'un bug où la sélection de filtre sur la page d'index pouvait être déclenchée deux fois. [#3344](https://github.com/gip-inclusion/rdv-insertion/issues/3344)

### Évolutions techniques
- Amélioration de la performance de l'endpoint d'index des utilisateurs. [#3358](https://github.com/gip-inclusion/rdv-insertion/issues/3358)
- Asynchronisation de l'expiration des invitations pour améliorer la réactivité. [#3357](https://github.com/gip-inclusion/rdv-insertion/issues/3357)
- Augmentation du délai d'attente pour les migrations de la base de données, notamment pour la migration des origines des invitations. [#3343](https://github.com/gip-inclusion/rdv-insertion/issues/3343)
- Mise à jour de plusieurs dépendances (rails-html-sanitizer, etc.). [#3348](https://github.com/gip-inclusion/rdv-insertion/issues/3348)

### Autres changements
- Mise à jour de la documentation du schéma de données avec l'origine des données. [#3342](https://github.com/gip-inclusion/rdv-insertion/issues/3342)
- Correction de la migration pour appliquer l'index en dernier.
