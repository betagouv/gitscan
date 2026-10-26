## Changelog : projects (30 derniers jours, au 19 octobre 2026)

### Résumé
Les récentes mises à jour se concentrent sur l'amélioration de la gestion des commentaires et de la visibilité des activités pour les utilisateurs en lecture seule. Parallèlement, des mesures de sécurité importantes ont été appliquées à l'infrastructure de production pour corriger des vulnérabilités.

### Évolutions fonctionnelles
- **Gestion des commentaires** : les propriétaires de tableau peuvent désormais supprimer n'importe quel commentaire sur leur tableau [#112](https://github.com/suitenumerique/projects/issues/112).
- **Visibilité des activités** : les utilisateurs disposant d'un droit de consultation (sans droit d'écriture) peuvent désormais voir les commentaires et l'historique des activités sur les cartes [#111](https://github.com/suitenumerique/projects/issues/111).

### Évolutions techniques
- **Sécurité** : correction de vulnérabilités (CVE) dans l'image de production via la mise à jour de Node.js, l'application de correctifs Alpine et la mise à jour des dépendances serveur.
- **Infrastructure** : extension de la période de vérification de santé (*healthcheck*) de Keycloak à 300s pour fiabiliser le démarrage du service [#110](https://github.com/suitenumerique/projects/issues/110).
