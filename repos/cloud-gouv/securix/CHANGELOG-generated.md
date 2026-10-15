## Changelog : securix (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, SecurixOS a bénéficié de plusieurs améliorations visant à renforcer la fiabilité du système et à enrichir l'expérience utilisateur. Les mises à jour automatiques sont désormais plus robustes, de nouveaux outils de gestion pour les clés Yubikey ont été intégrés, et l'interface utilisateur a été affinée, notamment pour la gestion des raccourcis clavier et l'écran de connexion.

### Évolutions fonctionnelles
- **Nouveaux outils communautaires** : Ajout d'un outil pour la réinitialisation des clés Yubikey [#302](https://github.com/cloud-gouv/securix/issues/302).
- **Interface utilisateur** :
    - Amélioration de la gestion des raccourcis clavier dans l'environnement Sway via l'utilisation des codes de touches [#262](https://github.com/cloud-gouv/securix/issues/262).
    - Masquage des comptes administrateurs sur l'écran de connexion SDDM pour plus de discrétion [#265](https://github.com/cloud-gouv/securix/issues/265).

### Évolutions techniques
- **Fiabilisation des mises à jour automatiques** : 
    - Mise en place d'une stratégie de tentatives avec backoff exponentiel et meilleure gestion de la suppression des anciennes versions du système [#276](https://github.com/cloud-gouv/securix/issues/276).
    - Correction d'un problème de temporisation dans le module de récupération automatique [#277](https://github.com/cloud-gouv/securix/issues/277).
- **Réseau et Sécurité** :
    - Optimisation de la correspondance des noms de domaine (DN) pour les connexions IPsec, indépendamment de leur ordre [#279](https://github.com/cloud-gouv/securix/issues/279).
    - Implémentation d'un système de rapport de télémétrie de base pour la communauté.
- **Système et Robustesse** :
    - Optimisation de la gestion de la fréquence CPU pour les machines de type x13 [#273](https://github.com/cloud-gouv/securix/issues/273).
    - Corrections de diverses erreurs d'évaluation Nix [#269](https://github.com/cloud-gouv/securix/issues/269), de conditions dans l'installateur automatique [#267](https://github.com/cloud-gouv/securix/issues/267), du générateur d'inventaire [#303](https://github.com/cloud-gouv/securix/issues/303) et de la gestion des utilisateurs via sudo [#284](https://github.com/cloud-gouv/securix/issues/284).

### Autres changements
- **Documentation** : Corrections typographiques dans le fichier README [#297](https://github.com/cloud-gouv/securix/issues/297).
- **Configuration** : Ajout de nouveaux modules par défaut à la section communautaire.
