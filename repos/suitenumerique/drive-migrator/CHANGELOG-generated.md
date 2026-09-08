## Changelog : drive-migrator (30 derniers jours, au 04/09/2026)

### Résumé
Les récentes évolutions se concentrent sur la fiabilité des migrations et la sécurité. L'outil est désormais plus résilient face aux erreurs de téléchargement et propose une gestion administrative plus complète, tout en modernisant ses protocoles d'authentification.

### Évolutions fonctionnelles
- **Administration renforcée** : ajout de la recherche par nom/email dans la liste des utilisateurs et nouvelles actions pour réinitialiser les connexions Resana ou Drive [#198].
- **Expérience utilisateur améliorée** : nouveau parcours de téléchargement des archives ZIP [#194], ajout d'infobulles pour les titres longs [#195] et clarification des messages d'erreur et des cibles de migration [#140, #193].
- **Résilience des exports** : en cas d'échec du téléchargement d'un fichier, le processus d'exportation continue désormais au lieu de s'interrompre, tout en enregistrant les erreurs pour suivi.
- **Correction d'interface** : résolution d'un problème de boucle infinie sur la modale d'erreur lors de la connexion.

### Évolutions techniques
- **Sécurité et Authentification** : implémentation du protocole PKCE pour sécuriser et stabiliser les connexions avec le client Resana.
- **Fiabilité du système** : ajout de mécanismes de tentatives automatiques (retries) lors des téléchargements de fichiers en cas d'erreurs réseau temporaires.
- **Maintenance et Refactoring** : optimisation de la gestion des jetons (tokens), correction de plantages dans l'interface d'administration et résolution de problèmes de configuration des variables d'environnement.
- **Optimisation S3** : suppression des en-têtes non signés lors des téléchargements via des liens présignés S3.

### Autres changements
- Corrections de fautes de frappe dans les modèles d'emails de notification.
- Ajustements visuels sur la page de fin de processus [#207].
