## Changelog : fondation (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'une amélioration notable de son interface utilisateur et de la gestion des documents officiels. La sécurité a été renforcée, notamment sur l'authentification et la protection des données, tandis qu'un effort important a été porté sur la fiabilité du système via l'extension massive des tests automatisés et la modernisation de l'environnement technique.

### Évolutions fonctionnelles
- **Interface et expérience utilisateur** :
    - Modernisation des tableaux avec l'intégration de DataTable et unification des écrans de secrétariat et d'administration [#726](https://github.com/betagouv/fondation/issues/726).
    - Amélioration de la recherche de magistrats directement depuis la navigation [#719](https://github.com/betagouv/fondation/issues/719).
    - Affichage plus clair des informations de session (badges de formation, accès aux sessions archivées) [#697](https://github.com/betagouv/fondation/issues/697), [#728](https://github.com/betagouv/fondation/issues/728).
    - Optimisation de l'affichage des noms (Prénom et Nom marital) et des numéros de téléphone des magistrats [#691](https://github.com/betagouv/fondation/issues/691), [#682](https://github.com/betagouv/fondation/issues/682).
- **Gestion documentaire et rapports** :
    - Amélioration de la rédaction des rapports officiels : ajout de notes sous les propositions [#772](https://github.com/betagouv/fondation/issues/772), gestion des pluriels dans les ouvertures de rapports [#769](https://github.com/betagouv/fondation/issues/769) et support des sauts de ligne dans les blocs de documents [#671](https://github.com/betagouv/fondation/issues/671).
    - Meilleure visibilité sur le statut des documents et des agendas à présenter [#720](https://github.com/betagouv/fondation/issues/720), [#605](https://github.com/betagouv/fondation/issues/605).
    - Restriction des droits pour les rapporteurs (impossibilité de prendre des notes personnelles) [#714](https://github.com/betagouv/fondation/issues/714).
- **Administration et communication** :
    - Nouveaux pouvoirs pour les administrateurs : désactivation de comptes et déconnexion forcée des utilisateurs lors d'un changement de mot de passe [#764](https://github.com/betagouv/fondation/issues/764).
    - Migration des alertes de la plateforme vers Tchap [#689](https://github.com/betagouv/fondation/issues/689).
    - Mise en place de sondages de satisfaction pour les utilisateurs après chaque session [#686](https://github.com/betagouv/fondation/issues/686), [#681](https://github.com/betagouv/fondation/issues/681).

### Évolutions techniques
- **Sécurité** :
    - Renforcement de la robustesse de l'authentification (protection contre les tentatives de devinettes et gestion des caractères spéciaux) [#732](https://github.com/betagouv/fondation/issues/732).
    - Nettoyage (sanitization) systématique du HTML pour les rapports, résumés et commentaires afin de prévenir les injections [#762](https://github.com/betagouv/fondation/issues/762), [#759](https://github.com/betagouv/fondation/issues/759).
    - Correction de vulnérabilités sur les dépendances `multer` et `qs` [#673](https://github.com/betagouv/fondation/issues/673).
- **Tests et fiabilité** :
    - Extension massive de la couverture de tests de bout en bout (E2E) couvrant les comptes, les sessions, les pièces jointes, les résumés et les rapports officiels [#755](https://github.com/betagouv/fondation/issues/755), [#754](https://github.com/betagouv/fondation/issues/754), [#753](https://github.com/betagouv/fondation/issues/753), [#752](https://github.com/betagouv/fondation/issues/752), [#751](https://github.com/betagouv/fondation/issues/751), [#750](https://github.com/betagouv/fondation/issues/750), [#737](https://github.com/betagouv/fondation/issues/737), [#736](https://github.com/betagouv/fondation/issues/736).
- **Architecture et infrastructure** :
    - Migration du monorepo vers TypeScript 7 [#766](https://github.com/betagouv/fondation/issues/766).
    - Refactorisation pour réduire les cycles d'importation entre les modules et favoriser une communication via des services dédiés [#695](https://github.com/betagouv/fondation/issues/695), [#692](https://github.com/betagouv/fondation/issues/692).
    - Optimisation de l'envoi des événements Sentry pour contourner les bloqueurs de publicité [#763](https://github.com/betagouv/fondation/issues/763).
    - Amélioration de la gestion du stockage (nettoyage des fichiers orphelins) [#757](https://github.com/betagouv/fondation/issues/757), [#733](https://github.com/betagouv/fondation/issues/733).

### Autres changements
- **Documentation** : Mise à jour de la documentation sur les règles métier et les procédures d'importation des données LOLFI [#749](https://github.com/betagouv/fondation/issues/749), [#684](https://github.com/betagouv/fondation/issues/684).
- **Outils** : Amélioration de l'environnement Storybook pour le développement de l'interface [#748](https://github.com/betagouv/fondation/issues/748).
