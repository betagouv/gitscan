## Changelog : ami-fc-proxy (30 derniers jours, au 14 août 2026)

### Résumé
Les récentes évolutions se concentrent sur la fiabilisation du mécanisme de redirection et l'optimisation des processus de déploiement et de configuration, rendant l'outil plus robuste et plus facile à installer localement.

### Évolutions fonctionnelles
- Correction de la génération de l'URL de redirection (`redirect_uri`) pour assurer une compatibilité correcte avec la gestion des fragments et des paramètres de requête par le framework Litestar [#26](https://github.com/numerique-gouv/ami-fc-proxy/pull/26).

### Évolutions techniques
- Migration de la gestion de la configuration vers l'utilisation de variables d'environnement [#1095](https://github.com/numerique-gouv/ami-fc-proxy/pull/1095).
- Optimisation du déploiement sur les conteneurs Scalingo en supprimant l'usage de `uv` [#1088](https://github.com/numerique-gouv/ami-fc-proxy/pull/1088).

### Autres changements
- Ajout d'un fichier `.env.local.template` pour faciliter la configuration des environnements de développement locaux [#1095](https://github.com/numerique-gouv/ami-fc-proxy/pull/1095).
