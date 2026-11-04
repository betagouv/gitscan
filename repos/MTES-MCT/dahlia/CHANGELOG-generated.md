## Changelog : dahlia (30 derniers jours, au 02 novembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'interface utilisateur et l'ajout de fonctionnalités clés comme la gestion des favoris et la classification automatique des dossiers. La sécurité et la stabilité du système ont également été renforcées, notamment par une meilleure gestion des accès et la mise en place de protections contre les appels excessifs aux services externes.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : Ajout de la gestion des favoris [#213], de la récupération des dossiers liés [#209], de la classification lors du scrapping [#215], de nouveaux blocs de qualification et de commentaires [#197], ainsi que d'un accès direct au formulaire de retour utilisateur [#180].
- **Interface et expérience utilisateur** : Refonte de l'interface générale [#225], réorganisation des onglets [#195] et de la barre latérale [#212], amélioration de l'affichage des informations du dossier [#196, #202], modification du header des pièces jointes [#211] et renommage automatique des fichiers selon les standards Télérecours [#208].
- **Gestion métier** : Intégration du type de litige "injonction" dans les règles de gestion [#194].

### Évolutions techniques
- **Sécurité et conformité** : Renforcement des contrôles d'accès (administration et validité de session) [#226, #171, #186], ajout de logs d'audit pour les refus d'accès [#174], assainissement des noms de fichiers dans les exports [#229] et application de mises à jour de sécurité critiques [#230].
- **Stabilité et infrastructure** : Implémentation de limitations de débit (rate limiting) pour les appels vers Télérecours [#227, #187], ajout d'une tâche planifiée (cron) pour le département 93 [#188] et alignement de la version Node.js avec l'environnement de production [#217].
- **Architecture et authentification** : Évolution de la structure de la base de données (clé primaire incluant le code de juridiction) [#175] et optimisation du processus de déconnexion via ProConnect [#224, #169].

### Autres changements
- Correction du script de détection des décisions [#183].
- Dépréciation de messages de limite de débit obsolètes [#228].
- Résolution de problèmes d'affichage d'erreurs trop verbeuses [#173].
