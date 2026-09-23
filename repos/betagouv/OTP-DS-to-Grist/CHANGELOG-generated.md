## Changelog : OTP-DS-to-Grist (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, le connecteur a gagné en puissance avec l'introduction de la synchronisation automatique pour plusieurs démarches simultanées et l'ajout de filtres multiples. Nous avons également renforcé la fiabilité du système en corrigeant des problèmes de perte de données et en améliorant l'assistance utilisateur grâce à la mise à jour des agents intelligents.

### Évolutions fonctionnelles
- **Synchronisation et filtrage :** gestion de la synchronisation automatique pour plusieurs démarches en parallèle ([#491](https://github.com/betagouv/OTP-DS-to-Grist/issues/491)) et ajout de la possibilité d'utiliser plusieurs filtres ([#459](https://github.com/betagouv/OTP-DS-to-Grist/issues/459)).
- **Fiabilité :** correction d'un bug provoquant la perte de données dans les champs de type "carte" ([#497](https://github.com/betagouv/OTP-DS-to-Grist/issues/497)).
- **Assistance :** mise à jour des agents d'aide (IA) et amélioration de la gestion des liens d'aide via des variables d'environnement ([#487](https://github.com/betagouv/OTP-DS-to-Grist/issues/487)).

### Évolutions techniques
- **Refactorisation et optimisation :** extraction de la classe `ColumnCache` ([#472](https://github.com/betagouv/OTP-DS-to-Grist/issues/472)) et nettoyage du code via la suppression de code mort et de routes inutilisées ([#477](https://github.com/betagouv/OTP-DS-to-Grist/issues/477), [#478](https://github.com/betagouv/OTP-DS-to-Grist/issues/478)).
- **Architecture :** mise en place de sous-agents pour le module Opencode ([#501](https://github.com/betagouv/OTP-DS-to-Grist/issues/501)).

### Autres changements
- **Maintenance et environnement :** optimisation de la configuration Docker et de l'environnement Codespace ([#509](https://github.com/betagouv/OTP-DS-to-Grist/issues/509)), maintenance du module DN ([#515](https://github.com/betagouv/OTP-DS-to-Grist/issues/515)) et mise à jour de la documentation.
