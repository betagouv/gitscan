## Changelog : fondation (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur la fiabilisation de la gestion des déports (recusals), le renforcement de la sécurité des comptes utilisateurs et l'optimisation de la gestion documentaire. L'outil est devenu plus robuste face aux erreurs de saisie et plus protecteur concernant les données sensibles.

### Évolutions fonctionnelles

**Gestion des déports (recusals)**
- Amélioration complète du suivi des membres déportés : enregistrement de l'auteur des changements [#861](https://github.com/betagouv/fondation/issues/861), mention des membres déportés dans les rapports officiels avec leurs titres administratifs [#860](https://github.com/betagouv/fondation/issues/860) et sous chaque proposition du rapport [#856](https://github.com/betagouv/fondation/issues/856).
- Ajout d'alertes de sécurité pour le secrétariat lorsqu'un membre déporté est affecté à un dossier [#859](https://github.com/betagouv/fondation/issues/859).
- Possibilité de gérer les déports en masse sur plusieurs dossiers de nomination simultanément [#847](https://github.com/betagouv/fondation/issues/847).
- Amélioration de l'interface pour confirmer les déports via le panneau latéral ou des actions groupées [#854](https://github.com/betagouv/fondation/issues/854).

**Gestion des utilisateurs et des comptes**
- Refonte de la gestion des utilisateurs et de l'affichage de l'historique des comptes (auteur des modifications) [#825](https://github.com/betagouv/fondation/issues/825), [#833](https://github.com/betagouv/fondation/issues/833).
- Nouveaux contrôles administratifs : création de comptes depuis la liste des utilisateurs [#804](https://github.com/betagouv/fondation/issues/804), désactivation de comptes et déconnexion forcée des utilisateurs [#764](https://github.com/betagouv/fondation/issues/764).
- Autonomie accrue : les utilisateurs peuvent désormais modifier leur propre mot de passe via une page dédiée [#800](https://github.com/betagouv/fondation/issues/800).
- Renforcement de la sécurité des connexions : protection contre les tentatives de force brute par adresse ou par IP [#844](https://github.com/betagouv/fondation/issues/844), [#732](https://github.com/betagouv/fondation/issues/732).

**Gestion documentaire et fichiers**
- Amélioration de l'expérience d'upload : support du glisser-déposer n'importe où dans la zone de téléchargement [#836](https://github.com/betagouv/fondation/issues/836).
- Mise en place de limites strictes pour éviter la saturation : plafonnement du nombre de fichiers (20 max) et de leur taille (50 Mo par défaut) avec avertissements utilisateurs [#831](https://github.com/betagouv/fondation/issues/830), [#835](https://github.com/betagouv/fondation/issues/835).
- Nettoyage automatique des fichiers orphelins dans le stockage pour libérer de l'espace [#843](https://github.com/betagouv/fondation/issues/843), [#757](https://github.com/betagouv/fondation/issues/757), [#733](https://github.com/betagouv/fondation/issues/733).

**Expérience utilisateur (UI/UX)**
- Création d'un centre d'aide rédigé par les administrateurs [#808](https://github.com/betagouv/fondation/issues/808).
- Unification des interfaces de l'administration et du secrétariat via l'utilisation de composants de tableaux standardisés [#726](https://github.com/betagouv/fondation/issues/726).
- Amélioration de la navigation : recherche de magistrats par nom directement depuis la barre de navigation [#719](https://github.com/betagouv/fondation/issues/719).
- Meilleure visibilité des sessions archivées pour les membres [#728](https://github.com/betagouv/fondation/issues/728).

### Évolutions techniques

**Sécurité et conformité**
- Renforcement de la politique de sécurité du contenu (CSP) sur le client et l'API, avec remontée des violations vers Sentry [#864](https://github.com/betagouv/fondation/issues/864), [#817](https://github.com/betagouv/fondation/issues/817).
- Protection de la confidentialité des données : suppression de l'envoi de données sensibles (query strings, corps de requêtes, cookies, headers) vers Sentry [#819](https://github.com/betagouv/fondation/issues/819), [#811](https://github.com/betagouv/fondation/issues/811), [#818](https://github.com/betagouv/fondation/issues/818).
- Mise à jour critique de Node.js pour corriger une vulnérabilité (CVE) [#806](https://github.com/betagouv/fondation/issues/806).

**Architecture et refactoring**
- Optimisation de la structure du code : découplage des modules pour une communication via services plutôt que des imports directs, réduisant les cycles d'importation [#692](https://github.com/betagouv/fondation/issues/692), [#695](https://github.com/betagouv/fondation/issues/695).
- Refactorisation de la gestion des priorités des dossiers de nomination pour les isoler de l'affectation [#758](https://github.com/betagouv/fondation/issues/758).

**Qualité logicielle et CI/CD**
- Augmentation significative de la couverture des tests de bout en bout (E2E) sur les parcours critiques : gestion des comptes, impersonnalisation, sessions et documents [#755](https://github.com/betagouv/fondation/issues/755), [#754](https://github.com/betagouv/fondation/issues/754), [#753](https://github.com/betagouv/fondation/issues/753), [#752](https://github.com/betagouv/fondation/issues/752), [#751](https://github.com/betagouv/fondation/issues/750), [#737](https://github.com/betagouv/fondation/issues/737), [#736](https://github.com/betagouv/fondation/issues/736).
- Automatisation de la synchronisation des clients OpenAPI [#862](https://github.com/betagouv/fondation/issues/862), [#799](https://github.com/betagouv/fondation/issues/799), [#730](https://github.com/betagouv/fondation/issues/730).
- Amélioration du processus de déploiement vers l'environnement de staging [#701](https://github.com/betagouv/fondation/issues/701).

### Autres changements
- Mise à jour de la documentation technique et des conventions de code [#773](https://github.com/betagouv/fondation/issues/773), [#749](https://github.com/betagouv/fondation/issues/749).
- Nettoyage de la base de données (suppression d'index et de scripts obsolètes) [#760](https://github.com/betagouv/fondation/issues/760), [#708](https://github.com/betagouv/fondation/issues/708).
