## Changelog : ds_proxy (30 derniers jours, au 12 juin 2026)

### Résumé
Cette version apporte une correction importante concernant la gestion des en-têtes HTTP lors du proxyage des requêtes. Un en-tête spécifique, `content-md5`, était modifié par le proxy, ce qui pouvait entraîner des problèmes d'intégrité des données. Cette correction assure que l'en-tête est correctement supprimé avant d'être transmis.

### Évolutions fonctionnelles
- Correction d'un bug où l'en-tête `content-md5` était altéré lors du proxyage, ce qui pouvait impacter l'intégrité des fichiers [#150](https://github.com/demarche-numerique/ds_proxy/pull/150).

### Évolutions techniques
- Mise à jour des dépendances du projet.
- Adaptations mineures suite à la mise à jour des dépendances.

### Autres changements
- Aucune information supplémentaire.
