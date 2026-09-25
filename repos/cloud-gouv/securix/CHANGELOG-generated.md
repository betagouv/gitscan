## Changelog : securix (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois-ci, Securix a franchi une étape importante avec une refonte complète de sa documentation pour la rendre bilingue (français/anglais) et plus accessible. L'expérience utilisateur a été améliorée, notamment pour la gestion du VPN et l'interface de connexion, tandis que la sécurité et la stabilité du système ont été renforcées par plusieurs correctifs techniques et optimisations de l'installation.

### Évolutions fonctionnelles
- **Amélioration de l'interface de connexion** : masquage des comptes administrateurs dans l'écran de connexion SDDM pour plus de discrétion [#265](https://github.com/cloud-gouv/securix/issues/265).
- **Gestion du VPN (Wireguard)** : affichage de la clé publique via un QR code pour faciliter les processus de configuration [#234](https://github.com/cloud-gouv/securix/issues/234).
- **Personnalisation de l'environnement** : amélioration de la gestion des raccourcis clavier sous Sway via l'utilisation des codes de touches (keycode) [#262](https://github.com/cloud-gouv/securix/issues/262).

### Évolutions techniques
- **Renforcement de la sécurité SSH** : désactivation de l'authentification par mot de passe pour `sshd` et restriction de la gestion des tunnels SSH via l'option `auth.sshForward`.
- **Sécurisation de l'installateur** : correction de l'estampillage des clés SSH de l'hôte avec le nom d'hôte cible [#235](https://github.com/cloud-gouv/securix/issues/235).
- **Optimisation du système** : mise en place du nettoyage automatique (garbage collection) des anciennes générations de configuration pour libérer de l'espace [#202](https://github.com/cloud-gouv/securix/issues/202).
- **Refactoring et architecture** : exposition des outils via un module dédié pour une meilleure modularité [#221](https://github.com/cloud-gouv/securix/issues/221).
- **Corrections de stabilité** : résolution d'erreurs d'évaluation [#269](https://github.com/cloud-gouv/securix/issues/269), correction de conditions dans l'outil d'autoinstallation [#267](https://github.com/cloud-gouv/securix/issues/267) et ajout de la dépendance Git pour le script de mise à jour [#251](https://github.com/cloud-gouv/securix/issues/251).

### Autres changements
- **Refonte majeure de la documentation** : passage au bilingue (français/anglais), ajout de nouveaux guides d'ingénierie et de déploiement, intégration du support Mermaid pour les diagrammes et ajout d'un sélecteur de langue [#230](https://github.com/cloud-gouv/securix/issues/230) [#231](https://github.com/cloud-gouv/securix/issues/231).
- **Nettoyage du code** : suppression de variables inutilisées [#248](https://github.com/cloud-gouv/securix/issues/248) et ajustement des règles de formatage pour ignorer certains dossiers non pertinents [#252](https://github.com/cloud-gouv/securix/issues/252).
