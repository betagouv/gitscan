## Changelog : egapro (30 derniers jours, au 11 novembre 2026)

### Résumé
Ce mois a été marqué par un effort massif de mise en conformité de l'accessibilité numérique et par l'amélioration de la fiabilité des parcours de déclaration (rémunération, représentation et avis CSE). Les utilisateurs bénéficient désormais de documents PDF récapitulatifs plus complets et d'une navigation plus fluide, tandis que les administrateurs disposent de nouveaux leviers de pilotage pour les campagnes.

### Évolutions fonctionnelles

* **Déclarations et parcours utilisateurs**
    - Amélioration de la génération et du design des documents PDF récapitulatifs (déclarations de représentation, avis CSE et données préremplies) [#5081](https://github.com/SocialGouv/egapro/issues/5081), [#5097](https://github.com/SocialGouv/egapro/issues/5097), [#4830](https://github.com/SocialGouv/egapro/issues/4830).
    - Optimisation des étapes de déclaration (rémunération, représentation, avis CSE) avec des libellés clarifiés et une meilleure gestion de la navigation [#5153](https://github.com/SocialGouv/egapro/issues/5153), [#5139](https://github.com/SocialGouv/egapro/issues/5139), [#4983](https://github.com/SocialGouv/egapro/issues/4983).
    - Ajout d'informations sur les délais de verrouillage avant de pouvoir reprendre une déclaration [#5085](https://github.com/SocialGouv/egapro/issues/5085).
    - Affichage systématique du sens des écarts de rémunération sur l'ensemble des vues [#4842](https://github.com/SocialGouv/egapro/issues/4842).
    - Amélioration de la gestion des effectifs pour éviter les erreurs de saisie lors de la première étape [#4906](https://github.com/SocialGouv/egapro/issues/4906).

* **Espace utilisateur ("Mon espace")**
    - Amélioration de la visibilité des déclarations et des avis transmis dans le tableau de bord [#4900](https://github.com/SocialGouv/egapro/issues/4900), [#4950](https://github.com/SocialGouv/egapro/issues/4950).
    - Mise à jour de l'interface du profil et du panneau latéral pour une meilleure cohérence visuelle [#4903](https://github.com/SocialGouv/egapro/issues/4903), [#4976](https://github.com/SocialGouv/egapro/issues/4976).

* **Administration et Observatoire**
    - Nouveaux outils de pilotage pour les administrateurs : paramétrage des dates limites de parcours et suivi précis du statut des démarches [#5151](https://github.com/SocialGouv/egapro/issues/5151), [#5090](https://github.com/SocialGouv/egapro/issues/5090).
    - Amélioration de l'export des référents en format CSV [#5108](https://github.com/SocialGouv/egapro/issues/5108).
    - Ajout de l'historique des SIREN dans l'Observatoire pour faciliter l'audit RGAA [#5079](https://github.com/SocialGouv/egapro/issues/5079).

* **Accessibilité (A11y)**
    - Mise en conformité majeure de l'interface : amélioration de la navigation au clavier, de la structure des tableaux et graphiques, de la gestion des erreurs et de la compatibilité avec les lecteurs d'écran [#5001](https://github.com/SocialGouv/egapro/issues/5001) à [#5084](https://github.com/SocialGouv/egapro/issues/5084).

### Évolutions techniques

* **Sécurité et Authentification**
    - Renforcement de la sécurité : mise en place du MFA pour les déclarants et support des protocoles eidas2/eidas3 pour l'administration [#5132](https://github.com/SocialGouv/egapro/issues/5132), [#4816](https://github.com/SocialGouv/egapro/issues/4816).
    - Mise à jour de Node.js pour répondre aux derniers correctifs de sécurité [#4939](https://github.com/SocialGouv/egapro/issues/4939).
    - Anonymisation des données personnelles transmises à l'outil de monitoring Sentry [#4902](https://github.com/SocialGouv/egapro/issues/4902).

* **Infrastructure et Base de données**
    - Migration des environnements de développement vers PostgreSQL 17 [#4871](https://github.com/SocialGouv/egapro/issues/4871).
    - Optimisation de la gestion des journaux d'audit (durées de conservation et purge des accès administrateurs) [#5148](https://github.com/SocialGouv/egapro/issues/5148), [#4886](https://github.com/SocialGouv/egapro/issues/4886).

* **Qualité et CI/CD**
    - Amélioration de la couverture des tests de bout en bout (E2E), notamment sur les mécanismes de verrouillage des déclarations [#4911](https://github.com/SocialGouv/egapro/issues/4911).
    - Optimisation des workflows de CI pour inclure des tests d'accessibilité et de performance (Lighthouse) plus rigoureux [#5084](https://github.com/SocialGouv/egapro/issues/5084), [#4867](https://github.com/SocialGouv/egapro/issues/4867).

### Autres changements

* Mise à jour de la politique de confidentialité et versionnement des CGU [#4828](https://github.com/SocialGouv/egapro/issues/4828).
* Configuration d'outils d'assistance par IA pour optimiser le développement [#5096](https://github.com/SocialGouv/egapro/issues/5096).
