## Changelog : passemarche (30 derniers jours, au 7 août 2026)

### Résumé
Ce mois a été marqué par l'amélioration significative du cycle de vie des marchés, avec l'introduction de la possibilité de publier et de modifier les configurations de consultation. Les acheteurs disposent désormais d'un outil de synthèse PDF pour leurs configurations, et la fiabilité de l'application a été renforcée par des mises à jour de sécurité critiques et une optimisation des tests automatisés.

### Évolutions fonctionnelles
- **Gestion des marchés et publications** :
    - Ajout de la possibilité de publier une consultation et de verrouiller un marché via un nouveau bouton dédié dans l'éditeur ([#439](https://github.com/datagouv/passemarche/pull/439)).
    - Mise en place d'un service permettant la re-soumission d'un marché déjà complété ([#439](https://github.com/datagouv/passemarche/pull/439)).
    - Les candidats peuvent désormais visualiser les marchés publiés directement dans l'éditeur de test ([#471](https://github.com/datagouv/passemarche/pull/471)).
- **Synthèse et documentation** :
    - Génération et téléchargement d'un PDF de synthèse de la configuration acheteur ([#452](https://github.com/datagouv/passemarche/pull/452)).
    - Intégration des icônes de badges de scope dans les documents PDF générés ([#450](https://github.com/datagouv/passemarche/pull/450)).
    - Amélioration des formulations et ajout de rappels concernant les motifs d'exclusion dans les attestations ([#486](https://github.com/datagouv/passemarche/pull/486)).
- **Traçabilité et données** :
    - Historisation des modifications de lots et de la sélection des attributs par marché ([#458](https://github.com/datagouv/passemarche/pull/458)).
    - Inclusion des lots sélectionnés par le candidat dans les webhooks de candidature ([#475](https://github.com/datagouv/passemarche/pull/475)).
- **Corrections d'expérience utilisateur (UX/UI)** :
    - Correction de la persistance des choix "non" sur les champs optionnels ([#492](https://github.com/datagouv/passemarche/pull/492)).
    - Ajustements visuels sur l'interface : espacements des bandeaux d'erreur, largeur des boutons et comportement du sélecteur de types de lots ([#482](https://github.com/datagouv/passemarche/pull/482), [#481](https://github.com/datagouv/passemarche/pull/481)).

### Évolutions techniques
- **Sécurité** : Mise à jour de Rails vers la version 8.1.3.1 pour corriger une vulnérabilité (CVE-2026-66066) ([#485](https://github.com/datagouv/passemarche/pull/485)).
- **Performance CI/CD** : Parallélisation des tests RSpec et Cucumber dans la chaîne de CI pour accélérer les validations ([#451](https://github.com/datagouv/passemarche/pull/451)).
- **Architecture** :
    - Refactorisation de la logique de génération de PDF via l'extraction d'un module commun `PdfGeneratable` ([#452](https://github.com/datagouv/passemarche/pull/452)).
    - Sécurisation de la construction des URLs via l'utilisation d'un hôte canonique ([#460](https://github.com/datagouv/passemarche/pull/460)).
- **Développement** : Activation du feature flag pour le futur module "groupement" en environnement sandbox ([#483](https://github.com/datagouv/passemarche/pull/483)).

### Autres changements
- **Documentation** : Suppression de la documentation technique locale au profit des guides officiels sur guides.data.gouv.fr ([#473](https://github.com/datagouv/passemarche/pull/473)).
- **Nettoyage** : Suppression de code mort dans le modèle `MarketApplication` ([#468](https://github.com/datagouv/passemarche/pull/468)).
