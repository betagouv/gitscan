## Changelog : potentiel (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'importation de données depuis DataGouv, la gestion des garanties financières, la correction de bugs liés aux notifications et aux formulaires, ainsi que sur des optimisations techniques et des refactorings pour améliorer la stabilité et la maintenabilité du service. Plusieurs améliorations ont été apportées à l'interface utilisateur pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- **Garanties Financières :** Refonte des pages garanties financières pour une meilleure présentation et ergonomie [#4175].
- **Notifications :** Suppression des notifications inutiles pour les étapes de projet en cas de recours [#4179]. Correction d'un bug empêchant les co-contractants de recevoir les notifications hors de leur zone [#4178].
- **Attestation de conformité :** Modification de l'attestation de conformité [#4159].
- **Dépôt GF :** Ajout du dépôt dans la projection des Garanties Financières [#4156].
- **Copie d'ID Projet :** Possibilité pour les utilisateurs DREALS de copier l'identifiant du projet en production [#4151].
- **Actionnariat :** Ajout d'un nouveau type d'actionnariat et importation des données depuis DataGouv [#4090].
- **Mails Garanties Financières :** Ajout de nouveaux modèles d'emails pour les garanties financières [#4083].
- **Typologies d'installation :** Ajout d'un type "non précisé" pour les typologies d'installation agricoles [#4086].
- **Abandon Projet :** Amélioration du wording de l'infobox concernant l'autorité compétente en cas d'abandon [#4087].

### Évolutions techniques
- **Import DN :** Import des références de raccordement et des détails de candidature depuis DataGouv [#4103, #4096].
- **Cache GraphQL :** Implémentation d'un cache GraphQL pour améliorer les performances [#8dfec2dd].
- **Refactoring :** Simplification de la modélisation des Autorisations d'Opérer (AO) [#4147]. Refactoring de la gestion des documents [#4162].
- **Tests :** Implémentation des tests manquants pour les délais et recours [#4182].
- **CI/CD :** Désactivation de l'envoi d'emails en environnement CI pour éviter les spams [#4138].
- **Types :** Ajout et amélioration des types TypeScript pour une meilleure robustesse du code [#4098, #4078].
- **Suppression de code obsolète :** Suppression de scripts et de code inutilisés [#4162, #4097].

### Autres changements
- **Données de test :** Mise à jour des données de test [#4181, #02e7015d].
- **Documentation :** Amélioration de la documentation interne.
- **Corrections diverses :** Correction de plusieurs bugs mineurs et améliorations de la qualité du code.
- **Mise à jour des dépendances :** Mise à jour de certaines dépendances (dompurify, picomatch, basic-ftp).
