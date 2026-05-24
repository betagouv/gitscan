## Changelog : anssi-portail (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'interface utilisateur en adoptant les composants du Design System Français (DSFR) sur l'ensemble du site.  Des corrections de bugs et des améliorations de la robustesse ont également été apportées, notamment au niveau de la gestion des erreurs et des appels à des services externes. Des améliorations de sécurité ont été implémentées, notamment la validation des entrées et la mise à jour de dépendances.

### Évolutions fonctionnelles
- Le site utilise désormais les composants du Design System Français (DSFR) pour de nombreux éléments d'interface : boutons, fil d'Ariane, segments, onglets, formulaires, etc. Cela améliore la cohérence visuelle et l'accessibilité du site.
- Le menu "Catalogue" a été renommé pour plus de clarté.
- Les résultats des tests de maturité sont désormais affichés par défaut.
- Les guides sont maintenant affichés par défaut.
- Possibilité de filtrer sur les nouvelles collections.
- Les liens de partage sur LinkedIn ont été améliorés.
- L'encart de diagnostic a été reformulé.
- Correction de la validation du numéro de téléphone lors de l'inscription.
- Possibilité d'autoriser la désactivation de la validation SIRET.
- Correction de l'affichage des filtres actifs sur la page des financements.
- Correction de la sélection des exigences.
- Correction de la validation de la comparaison ReCyF.

### Évolutions techniques
- Mise à jour de nombreuses dépendances pour corriger des failles de sécurité et bénéficier des dernières améliorations (axios, dompurify, fast-xml-parser, uuid, postcss, brace-expansion, devalue, fast-xml-builder).
- Refonte de la gestion des liens pour utiliser les composants DSFR.
- Amélioration de la robustesse des flux et de la gestion des erreurs, notamment en filtrant les erreurs réseau et celles provenant de services externes.
- Suppression de code obsolète et nettoyage de règles CSS inutilisées.
- Utilisation de Zod pour la validation des données et remplacement de `express-validator`.
- Amélioration du typage et de la gestion des erreurs de validation.
- Migration vers Corepack et support de Node.js 24.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Suppression des jobs d’approbation.
- Utilisation des valeurs paramétrées pour MQC.
- Ajout des différences dans l’artefact lors des appels à MQC.
- Amélioration de la gestion des erreurs de flux.
- Factorisation de l'édition des storages.
- Suppression de l'exposition de constantes internes.
- Éviter les erreurs de sécurité contextuelles.
- Suppression de certaines règles ESLint.
- Ajout d'une règle ESLint pour vérifier que les routes utilisent une validation de schéma.

### Autres changements
- Suppression de bruit dans Sentry pour améliorer la qualité des logs.
- Ajout d'une animation à l'encart des guides.
- Suppression d'une page de test.
- Mise à jour de la page des statistiques.
- Raccourcissement du wording d'une carte sur la page d'accueil.
- Déplacement des pages de promotions et des parcours dans le footer.
- Tris et simplification des surcharges de dépendance.
- Amélioration de la documentation.
- Correction du menu "parcours débuter".
- Ajout de liens d'évitement pour l'accessibilité.
- Suppression des styles du header.
- Ajustement des styles pour réduire le CLS (Cumulative Layout Shift).
- Ajout de la possibilité de décoder les entrées des ressources back.
- Suppression de la fonction d'aseptisation du middleware.
- Ajout de tests pour la validation du token.
- Renseignement d'un token valide pour les tests.
- Amélioration de la gestion des images dans les guides.
- Mise à jour de la version de l'UI Kit.
- Trace des clics sur les liens.
