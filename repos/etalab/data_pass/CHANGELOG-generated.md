## Changelog : data_pass (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois-ci, data_pass s'enrichit de nouveaux éditeurs de données (Ianord, Nexys, Dinum) et de nouveaux formulaires. L'expérience utilisateur est simplifiée par une interface de consultation plus claire et une terminologie plus explicite, tandis que la sécurité et la gestion des journaux système ont été renforcées.

### Évolutions fonctionnelles
- **Nouveaux éditeurs et formulaires** :
    - Intégration de l'éditeur Ianord et de ses formulaires pour les cantines lycées/collèges [#1710](https://github.com/etalab/data_pass/issues/1710).
    - Ajout du formulaire API Entreprise Nexys Relation Usagers (MGDIS) [#1731](https://github.com/etalab/data_pass/issues/1731).
    - Ajout du formulaire Dinum permettant de transmettre la convention aux contacts lors de la validation [#1691](https://github.com/etalab/data_pass/issues/1691).
- **Améliorations des formulaires existants** :
    - Ajout des scopes AEEH et régime pensionnat sur le formulaire CapDemat [#1709](https://github.com/etalab/data_pass/issues/1709).
    - Ajout du scope INE [#1722](https://github.com/etalab/data_pass/issues/1722).
- **Interface utilisateur (UI/UX)** :
    - Simplification des formulaires d'instruction : passage en mode consultation (suppression des boutons de modification et du panneau latéral) pour éviter les erreurs de saisie.
    - Amélioration de la visibilité : affichage des emails automatisés et explications sur les différents niveaux de droits.
    - Clarification de la terminologie : le champ « Nom de naissance » est désormais nommé « Nom de famille » [#1738](https://github.com/etalab/data_pass/issues/1738).
- **Corrections** :
    - Correction de la proactivité CNOUS pour utiliser le contact métier via le bridge HubEE.
    - Correction du paramètre par défaut des brouillons pour les instructeurs (désactivé par défaut).

### Évolutions techniques
- **Sécurité** : Mise à jour de Rails vers la version 8.1.3.1 pour corriger la vulnérabilité CVE-2026-66066 [#1715](https://github.com/etalab/data_pass/issues/1715).
- **Infrastructure et Observabilité** :
    - Migration de la production des journaux (logs) vers le format JSON via `logstasher`.
    - Suppression des configurations d'environnement locales (prod, staging, sandbox) pour s'appuyer sur la gestion par Ansible.
- **API et Documentation** :
    - Mise à jour de la documentation de l'API (cadres juridiques Ianord, correction du compteur du Socle général) [#1736](https://github.com/etalab/data_pass/issues/1736).
    - Clarification de la documentation des webhooks concernant la politique de retry [#1728](https://github.com/etalab/data_pass/issues/1728).
- **Authentification** : Ajustement de la gestion des scopes OAuth pour HubEE.

### Autres changements
- **Nettoyage** : Remplacement de l'attribut `cnous_statut_bourse` par `_boursier` pour une meilleure cohérence du code.
