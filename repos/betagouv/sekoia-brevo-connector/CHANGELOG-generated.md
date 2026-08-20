## Changelog : sekoia-brevo-connector (30 derniers jours, au 19 août 2026)

### Résumé
Lancement initial du connecteur permettant l'intégration des données Brevo vers la plateforme Sekoia. Les récents développements ont porté sur la mise en place de la structure du projet, la fiabilisation du processus de récupération des données et l'amélioration de la documentation.

### Évolutions fonctionnelles
- Mise à disposition de la première version du connecteur pour la récupération d'informations depuis Brevo.

### Évolutions techniques
- **Fiabilisation du traitement des données** : le traitement des données ne s'effectue désormais qu'en cas de succès de l'appel API, et les plages de dates (début et fin) sont recalculées automatiquement à chaque exécution.
- **Compatibilité des données** : modification de la représentation des données pour garantir leur sérialisation.
- **Qualité du code** : intégration de vérifications de types (typechecking) et corrections de la structure du code.

### Autres changements
- **Documentation** : ajout d'un script d'exemple, description du format des données reçues et documentation des commandes disponibles.
- **Configuration et initialisation** : mise en place de la structure du dépôt, configuration du fichier `pyproject.toml` et gestion des fichiers ignorés.
