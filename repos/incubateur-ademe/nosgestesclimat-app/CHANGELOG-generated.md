## Changelog : nosgestesclimat-app (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment sur la page de résultats avec l'ajout d'actions concrètes et l'amélioration de la présentation des données. Des corrections de bugs et des améliorations de sécurité ont également été apportées, ainsi que des optimisations techniques pour faciliter le développement et le déploiement. L'intégration des actions est en cours et se précise.

### Évolutions fonctionnelles
- Ajout d'un bloc d'actions à la fin du parcours, proposant des gestes à adopter pour réduire son impact [NGC-3408, #1869].
- Amélioration de l'affichage du graphique des catégories sur la page de résultats pour les groupes [NGC-3196, #1807].
- Possibilité de définir le mode simulation via l'URL [#1859].
- Implémentation d'une nouvelle question sur les tranches d'âge [#1788].
- Affichage du formulaire de contact en anglais [#1853].
- Mise à jour du texte des services publics sur la page des résultats [#1851].
- Amélioration de l'affichage des actions et de leur impact [NGC-3298, #1822].
- Ajout de la possibilité de partager l'URL avec des paramètres UTM pour le suivi [#1821].
- Amélioration de la gestion des régions via le paramètre `region` [#1824].

### Évolutions techniques
- Refonte du mécanisme de vérification pour le partage de données, utilisant une clé de vérification [NGC-3408, #1869].
- Migration de `restcountries` vers un package npm [#1847].
- Utilisation de `pnpm deploy` au lieu de `standalone` pour la production [#1831].
- Migration de `zod` vers `valibot` pour la validation de données [#1801].
- Ajout d'un worker pour le calcul des actions [#1811].
- Ajout d'un helper `createPage` et d'une règle ESLint pour renforcer l'utilisation des feature flags en tests E2E [#1840].
- Mise en place de tests E2E pour les actions [#1823].
- Ajout de la gestion des variantes de feature flags (tests A/B) [#1816].
- Ajout de migrations pour les utilisateurs anonymes (AnonUser et AnonPoll) [#1856].
- Correction d'un problème de crash des cookies lors de l'utilisation de `useFeatureFlag` en SSR [#1819].

### Autres changements
- Correction de plusieurs vulnérabilités de sécurité (redirections ouvertes, erreurs verbeuses) [#1871, #1854].
- Suppression du mode "jeune" (feature flag) [#1874].
- Suppression de liens morts [#1868, #1843].
- Amélioration du suivi des événements (auto-track) [#1852].
- Corrections de style et d'affichage sur différentes pages et composants [#1878, #1867, #1870, #1836].
- Améliorations diverses de l'interface utilisateur et du texte [#1849, #1803, #1809].
- Ajout d'un trigger manuel pour le déploiement de l'application [#1834].
- Correction du bouton de saut de la question d'âge [#1838].
- Ajout de suivi pour les actions [#1830].
- Mise à jour de la version du modèle [#1810].
- Correction du problème de mise à jour du cookie de langue [#1841].
- Amélioration de la cliquabilité du bloc d'actions sur la page de fin [#1805].
- Correction de bugs liés à l'iframe sur Safari [#1814].
- Ajout de la gestion de `pollMode` et `organisation` pour l'affichage des sondages anonymes [#1850].
- Correction du comportement du bouton "skip" sur la question d'âge [#1838].
