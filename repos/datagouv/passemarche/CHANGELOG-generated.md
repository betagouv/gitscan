## Changelog : passemarche (30 derniers jours, au 04 août 2026)

### Résumé
Ce mois-ci, passemarche a franchi une étape majeure en permettant aux acheteurs de publier et de modifier la configuration de leurs marchés directement depuis l'application. L'expérience utilisateur est enrichie par la génération de synthèses PDF de configuration, une meilleure visibilité sur le type de lots (via des badges colorés) et une gestion plus robuste des données pour les candidats, garantissant que leurs saisies manuelles ne soient pas perdues lors des mises à jour.

### Évolutions fonctionnelles
- **Gestion des marchés (Acheteurs) :**
    - Possibilité de publier une consultation et de modifier la configuration d'un marché ([#439](https://github.com/datagouv/passemarche/pull/439)).
    - Génération, affichage et téléchargement d'un document PDF de synthèse de la configuration acheteur ([#452](https://github.com/datagouv/passemarche/pull/452)).
    - Historisation des modifications de lots et de la sélection des attributs par marché ([#458](https://github.com/datagouv/passemarche/pull/458)).
    - Mise en conformité des libellés et des rappels concernant les motifs d'exclusion (wording DAJ) ([#486](https://github.com/datagouv/passemarche/pull/486)).
- **Expérience Candidat :**
    - Amélioration de la fiabilité des données : préservation des saisies manuelles (chiffre d'affaires, champs additionnels) lors de la re-candidature ou de la mise à jour des données par API ([#442](https://github.com/datagouv/passemarche/pull/442), [#449](https://github.com/datagouv/passemarche/pull/449)).
    - Gestion intelligente des exigences : les exigences liées à un type de lot sont automatiquement décochées si ce lot est retiré ([#465](https://github.com/datagouv/passemarche/pull/465)).
    - Clarification des messages d'erreur, notamment lorsqu'un marché n'est pas encore publié ([#472](https://github.com/datagouv/passemarche/pull/472)).
- **Interface et Design :**
    - Introduction de badges visuels (icônes et couleurs) pour identifier rapidement le périmètre des lots (travaux, services, fournitures) dans le wizard, les réponses et les documents PDF ([#448](https://github.com/datagouv/passemarche/pull/448), [#447](https://github.com/datagouv/passemarche/pull/447)).
    - Optimisation de l'interface : ajustements des espacements, de la largeur des boutons et comportement du sélecteur de type de lot ([#482](https://github.com/datagouv/passemarche/pull/482), [#481](https://github.com/datagouv/passemarche/pull/481)).

### Évolutions techniques
- **Sécurité :** Mise à jour de Rails vers la version 8.1.3.1 pour corriger une vulnérabilité critique ([#485](https://github.com/datagouv/passemarche/pull/485)).
- **API & Intégrations :**
    - Inclusion des lots sélectionnés par le candidat dans les webhooks de candidature ([#475](https://github.com/datagouv/passemarche/pull/475)).
    - Sécurisation de la construction des URLs via l'utilisation d'un hôte canonique ([#460](https://github.com/datagouv/passemarche/pull/460)).
    - Exposition de la synthèse de configuration via l'API éditeur et les webhooks ([#452](https://github.com/datagouv/passemarche/pull/452)).
    - Correction de la régénération automatique du PDF de synthèse lors de mises à jour via API ([#474](https://github.com/datagouv/passemarche/pull/474)).
- **Architecture & Refactoring :**
    - Mise en place d'un *feature flag* pour activer progressivement le module "groupement" ([#483](https://github.com/datagouv/passemarche/pull/483)).
    - Centralisation de la logique de génération de PDF dans un service partagé (`PdfGeneratable`) ([#452](https://github.com/datagouv/passemarche/pull/452)).
    - Utilisation de `paper_trail` pour assurer la traçabilité des modifications de lots ([#458](https://github.com/datagouv/passemarche/pull/458)).
    - Amélioration de la robustesse des migrations de base de données (idempotence et gestion des clés étrangères orphelines) ([#457](https://github.com/datagouv/passemarche/pull/457), [#469](https://github.com/datagouv/passemarche/pull/469)).

### Autres changements
- Nettoyage du code mort ([#468](https://github.com/datagouv/passemarche/pull/468)).
- Simplification de la documentation technique ([#473](https://github.com/datagouv/passemarche/pull/473)).
