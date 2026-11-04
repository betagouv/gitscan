## Changelog : fondation (30 derniers jours, au 03/11/2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la sécurité et de la confidentialité des données, notamment via une meilleure protection des accès et une gestion plus stricte des logs. L'expérience utilisateur a été fluidifiée par l'amélioration de la gestion des fichiers (glisser-déposer, limites de taille) et l'ajout d'outils d'aide et de support directement dans l'interface.

### Évolutions fonctionnelles
- **Gestion des fichiers et documents** : 
    - Introduction du glisser-déposer pour les téléchargements [#836](https://github.com/betagouv/fondation/issues/836).
    - Mise en place de limites strictes sur le nombre de fichiers (20 max) [#831](https://github.com/betagouv/fondation/issues/831) et la taille des pièces jointes (50 Mo) [#830](https://github.com/betagouv/fondation/issues/830) pour éviter les échecs d'envoi.
    - Amélioration de la fiabilité des documents (gestion des doublons, conservation des rapports validés) [#823](https://github.com/betagouv/fondation/issues/823) [#725](https://github.com/betagouv/fondation/issues/725).
- **Administration et gestion des utilisateurs** :
    - Refonte de la gestion des utilisateurs, incluant la création de comptes depuis la liste des utilisateurs [#825](https://github.com/betagouv/fondation/issues/825) [#804](https://github.com/betagouv/fondation/issues/804) et la possibilité de désactiver un compte [#764](https://github.com/betagouv/fondation/issues/764).
    - Affichage de l'historique des modifications par auteur sur les cartes d'utilisateurs [#833](https://github.com/betagouv/fondation/issues/833).
    - Meilleure visibilité des droits et actions selon le rôle de l'utilisateur [#774](https://github.com/betagouv/fondation/issues/774).
- **Aide et expérience utilisateur** :
    - Création d'un centre d'aide rédigé par les administrateurs [#808](https://github.com/betagouv/fondation/issues/808).
    - Ajout de conseils et d'avertissements contextuels dans l'éditeur de texte [#827](https://github.com/betagouv/fondation/issues/827).
    - Unification des interfaces de l'administration et du secrétariat via l'utilisation de DataTables [#726](https://github.com/betagouv/fondation/issues/726).
- **Communication et feedback** :
    - Migration des alertes vers Tchap au lieu de Mattermost [#689](https://github.com/betagouv/fondation/issues/689).
    - Mise en place de sondages de satisfaction pour les sessions [#686](https://github.com/betagouv/fondation/issues/686).
    - Possibilité d'envoyer des remarques depuis n'importe quelle page avec suivi administratif [#848](https://github.com/betagouv/fondation/issues/848).

### Évolutions techniques
- **Sécurité et confidentialité** :
    - Renforcement de la protection contre les attaques par force brute (suspension des accès après échecs répétés) [#844](https://github.com/betagouv/fondation/issues/844).
    - Sécurisation des logs Sentry : suppression des données sensibles (query strings, corps de requête, headers, cookies) pour garantir la confidentialité [#819](https://github.com/betagouv/fondation/issues/819) [#818](https://github.com/betagouv/fondation/issues/818) [#811](https://github.com/betagouv/fondation/issues/811).
    - Amélioration des en-têtes de sécurité (CSP, HSTS) [#817](https://github.com/betagouv/fondation/issues/817) et correction de vulnérabilités liées à la CSP [#845](https://github.com/betagouv/fondation/issues/845).
    - Mise à jour de Node.js pour corriger une vulnérabilité (CVE-2026-111497) [#806](https://github.com/betagouv/fondation/issues/806).
- **Architecture et maintenance** :
    - Migration du monorepo vers TypeScript 7 [#766](https://github.com/betagouv/fondation/issues/766).
    - Passage à la spécification OpenAPI 3.1 [#786](https://github.com/betagouv/fondation/issues/786).
    - Refactorisation de la communication entre modules via des services pour réduire les cycles d'importation [#692](https://github.com/betagouv/fondation/issues/692) [#695](https://github.com/betagouv/fondation/issues/695).
    - Automatisation du nettoyage nocturne des fichiers orphelins sur le stockage [#843](https://github.com/betagouv/fondation/issues/843) [#757](https://github.com/betagouv/fondation/issues/757).

### Autres changements
- Mise à jour de la documentation concernant les règles métier et les processus d'importation LOLFI [#749](https://github.com/betagouv/fondation/issues/749) [#684](https://github.com/betagouv/fondation/issues/684).
- Améliorations de l'environnement de test et de Storybook [#748](https://github.com/betagouv/fondation/issues/748).
