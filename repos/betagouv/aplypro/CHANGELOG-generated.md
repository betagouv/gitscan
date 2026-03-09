## Changelog : aplypro (30 derniers jours)

### Résumé
Les dernières mises à jour d'aplypro se concentrent sur l'amélioration de la gestion des adresses via l'intégration de l'API RNVP pour la normalisation, ainsi que sur la gestion des paiements et des rectifications, notamment pour les allocations ENPR. Des corrections de bugs et des améliorations de la qualité du code ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de joindre un fichier de correction d'adresse à une demande ([#1902](https://github.com/betagouv/aplypro/issues/1902)).
- Réactivation des paiements ENPR ([#1905](https://github.com/betagouv/aplypro/issues/1905)).
- Utilisation du champ `codeobjet` pour stocker la date PFMP et blocage des paiements de rectification négatifs en sortie ([#1896](https://github.com/betagouv/aplypro/issues/1896)).
- Le champ `codeobjet` est maintenant utilisé pour stocker la date PFMP ([#1892](https://github.com/betagouv/aplypro/issues/1892)).
- Journalisation des erreurs lors de la lecture des rectifications ([#1901](https://github.com/betagouv/aplypro/issues/1901)).
- Gestion des rectifications négatives : elles sont désormais conservées dans l'état "en attente".

### Évolutions techniques
- Intégration de l'API RNVP pour la normalisation des adresses ([#1735](https://github.com/betagouv/aplypro/issues/1735)).
- Adaptation de l'API RNVP à OAuth2.
- Déplacement de l'appel à RNVP dans le module 'lib'.
- Ajout de tests unitaires pour le module `Omogen::Rnvp`.
- Utilisation de `Omogen::Base` par l'API RUA.
- Gestion des timeouts et des erreurs lors des appels à l'API RNVP.
- Refactoring du code et correction des erreurs détectées par Rubocop.
- Ajout de nouveaux sous-types d'entités.

### Autres changements
- Mise à jour de la version à 2.8.7 et 2.8.8.
- Mise à jour des dépendances : nokogiri (1.19.0 -> 1.19.1), rack (3.2.4 -> 3.2.5), faraday (2.14.0 -> 2.14.1).
- Suppression des anciennes variables d'environnement "RUA_KC".
- Ajout de tests unitaires pour `Omogen::Rnvp`.
- Suppression de la configuration Codecov.
- Ajout de specs pour les nouvelles fonctionnalités.
