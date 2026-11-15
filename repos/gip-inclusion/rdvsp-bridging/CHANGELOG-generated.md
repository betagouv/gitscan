## Changelog : rdvsp-bridging (30 derniers jours, au 13 novembre 2026)

### Résumé
Ce mois a été marqué par une intégration majeure de Pipedrive, permettant désormais de créer des rendez-vous directement depuis l'outil CRM via un nouveau bouton "Prendre RDV". Le système de synchronisation a été considérablement renforcé pour importer automatiquement les bénéficiaires de Pipedrive vers RDV Service Public, tout en améliorant la gestion des organisations et la sécurité globale de la plateforme.

### Évolutions fonctionnelles
- **Intégration Pipedrive** :
    - Ajout d'un bouton "Prendre RDV" dans Pipedrive pour initier des rendez-vous et gérer l'installation de l'application [#19](https://github.com/gip-inclusion/rdvsp-bridging/pull/19).
    - Création automatique de plans de rendez-vous via l'API RDV-SP.
    - Liaison automatique des contacts Pipedrive avec les usagers RDV-SP par email ou téléphone.
    - Préfixage des identifiants externes des usagers avec le nom de l'entreprise Pipedrive pour éviter les collisions [#18](https://github.com/gip-inclusion/rdvsp-bridging/pull/18).
- **Gestion des usagers et synchronisation** :
    - Importation automatisée des bénéficiaires Pipedrive en tant qu'usagers RDV-SP [#16](https://github.com/gip-inclusion/rdvsp-bridging/pull/16).
    - Amélioration de la liaison entre les rendez-vous et les personnes physiques [#21](https://github.com/gip-inclusion/rdvsp-bridging/pull/21).
    - Possibilité d'ignorer les rendez-vous préexistants lors de la connexion pour éviter de synchroniser des données obsolètes [#10](https://github.com/gip-inclusion/rdvsp-bridging/pull/10).
- **Administration** :
    - Gestion des types d'activités de rendez-vous et des organisations RDV-SP directement depuis l'interface d'administration [#22](https://github.com/gip-inclusion/rdvsp-bridging/pull/22).
    - Meilleure visibilité sur les autorisations RDV-SP et l'état des imports d'usagers.

### Évolutions techniques
- **Sécurité et robustesse** :
    - Application de correctifs de sécurité critiques sur Rails, Ruby et d'autres dépendances [#9](https://github.com/gip-inclusion/rdvsp-bridging/pull/9) et [#2](https://github.com/gip-inclusion/rdvsp-bridging/pull/2).
    - Renforcement de la protection de l'administration via le rate limiting et sécurisation des mots de passe CalDAV (passage au SHA-256).
    - Mise en place de limites de taille de requête pour les webhooks afin de prévenir les attaques par déni de service.
- **Observabilité et fiabilité** :
    - Implémentation de tests de santé (smoke tests) automatisés après chaque déploiement [#14](https://github.com/gip-inclusion/rdvsp-bridging/pull/14).
    - Système d'alerte amélioré pour détecter les échecs d'importation ou les pertes de connexion avec RDV-SP.
    - Optimisation des migrations de base de données avec des timeouts de verrouillage pour garantir la disponibilité du service.
- **Infrastructure** :
    - Migration du domaine vers `pont-rdv.inclusion.gouv.fr` [#13](https://github.com/gip-inclusion/rdvsp-bridging/pull/13).
    - Configuration de la confiance envers les proxys Scaleway pour assurer la bonne transmission des en-têtes HTTP [#11](https://github.com/gip-inclusion/rdvsp-bridging/pull/11).

### Autres changements
- **Documentation** : Mise à jour complète de la documentation technique et fonctionnelle (configuration des activités, processus d'import, architecture).
- **Localisation** : Amélioration de la gestion du français dans les interfaces (règles de pluriel).
