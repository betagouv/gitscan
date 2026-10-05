## Changelog : account-manager (30 derniers jours, au 03 octobre 2026)

### Résumé
Ce mois-ci, l'outil a franchi une étape importante dans l'automatisation de la gestion des accès, notamment avec le retrait automatique des utilisateurs de plateformes comme GitHub et Notion. La visibilité sur les ressources possédées (comptes, dépôts, applications) a été considérablement renforcée, tout comme la précision du suivi des processus de transfert et de régularisation des droits.

### Évolutions fonctionnelles
- **Automatisation de l'offboarding** : Retrait automatique des membres des espaces de travail Notion [#147] et des organisations GitHub [#145].
- **Gestion des ressources et des comptes** :
    - Visualisation, collecte et déclaration de la capacité de lecture des objets possédés [#152, #148, #132].
    - Proposition de transfert de dépôts GitHub [#151].
    - Affichage des comptes personnels dans l'espace utilisateur [#120].
    - Administration des droits et couverture des collaborateurs sur Scalingo [#107, #101].
    - Rattachement de comptes "machine" aux systèmes correspondants [#106, #105].
- **Suivi des processus et conformité** :
    - Suivi précis de l'état des actions (confirmé, en cours, soldé) [#136] et des plans de geste [#129].
    - Signalement des accès maintenus au-delà du terme prévu [#146] ou des modèles de départ non relus [#122].
    - Gestion des dérogations (pose, levée et masquage des écarts couverts) [#94, #92].
    - Amélioration des processus de transfert (exigence d'un repreneur pour Scalingo [#134], correction du transfert d'applications possédées [#125]).
- **Améliorations de l'expérience utilisateur** :
    - Corrections de l'affichage des formulaires après refus [#144], de l'alignement des textes [#137, #113] et du thème des pages 404 [#112].
    - Clarification des demandes de liens d'accès [#82].

### Évolutions techniques
- **Architecture et Logique métier** :
    - Standardisation de la gestion des dates sur le fuseau horaire de Paris pour les comparaisons [#133].
    - Refonte de la logique de calcul des garde-fous, des tolérances et des plafonds d'interface [#143, #114, #98, #95, #108, #80].
    - Optimisation de la recherche de comptes via l'identifiant [#115].
- **Infrastructure et Build** :
    - Mise à jour de Next.js [#85] et intégration de nouveaux outils de build (nodemailer, vitest, fast-uri) [#87].
- **Tests** : Renforcement de la fiabilité et de la structure des tests (tests multi-étages, vérification visuelle des écrans et mutualisation des sessions) [#83, #116, #117, #89, #91, #88].

### Autres changements
- **Documentation** : Mise à jour des documents relatifs à l'architecture Scalingo, aux niveaux de configuration et aux limites de garde [#62f86f3, #6fe8bbd, #252a7f6, #90, #86].
- **Maintenance** : Uniformisation du vocabulaire utilisé dans l'ensemble des écrans de l'application [#84].
