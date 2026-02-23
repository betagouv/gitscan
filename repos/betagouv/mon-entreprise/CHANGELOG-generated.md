## Changelog : mon-entreprise (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions de mon-entreprise se concentrent sur l'amélioration de la précision des calculs pour les professionnels, notamment concernant la réforme RGDU, les exonérations d'heures supplémentaires et les cotisations spécifiques à certains secteurs. Des améliorations significatives ont également été apportées à l'accessibilité du site, avec une refonte complète de la documentation dédiée et des corrections d'implémentation. Enfin, le suivi analytique a été enrichi pour mieux comprendre l'utilisation des simulateurs.

### Évolutions fonctionnelles
- Implémentation de la réforme RGDU pour les salariés. (#f0df08a)
- Mise à jour de la déduction forfaitaire sur les heures supplémentaires. (#3da10e7)
- Ajout de la CET dans la base de l'exonération des heures supplémentaires. (#61eaaa7)
- Correction du taux de la flat tax affiché pour les dividendes. (#dc21af1)
- Correction de la saisie du taux Urssaf pour les chirurgiens-dentistes (PAMC). (#5e17902)
- Ajout de la date aux questions de la liste noire. (#0441ade)
- Suppression des taux réduits AF et AM hors Lodeom pour les salariés. (#a8b3e19)
- Suppression de l'avertissement concernant la réforme RGDU non implémentée. (#0c599cc)

### Évolutions techniques
- Refactorisation de l'utilisation de `inIframe()` au niveau module par `theme.isInIframe`. (#e2901b3)
- Remplacement de `console.error` par `Sentry.captureException` dans `colors.tsx` pour une meilleure gestion des erreurs. (#a560043)
- Suppression de la fonction `inIframe` devenue obsolète. (#9dbe2d1)
- Ajout d'une protection de type `window` dans `useIsEmbedded`. (#5998f99)
- Déplacement de l'accès à `document.location` dans un `useEffect`. (#0c43862)
- Amélioration de la vocalisation des questions dans le composant `<Questions />`. (#d9179d0)
- Amélioration du support de la vocalisation des étapes dans le composant `<Questions />`. (#05910f9)
- Refactorisation du composant `Questions` pour supprimer une prop inutilisée. (#94fabfe)
- Correction d'une faute de frappe et d'une importation implicite dans `AnswersList`. (#71522b4)

### Autres changements
- Mise à jour de la documentation sur l'accessibilité, avec des règles plus claires et des exemples concrets. (#ee5dcd1, #ed14440, #e9600d1, #e62e8cd, #e3c29e9, #db74575, #c871040, #c4ecca3, #c3e20fd, #9218daf, #881d9c5, #7b5ff5b, #7ac35b3, #72c3ea2, #727e3fc, #6d70cc7, #6c41a68, #5ee58f9, #5e5e16f, #5010755, #4fd3f2a, #4d46be0, #3ca9560, #32898ae, #2f05a67, #136576e, #0f457cd, #09896f7)
- Correction de bugs d'accessibilité, notamment remplacement d'un tableau par une liste. (#8ba5ccc)
- Mise à jour des traductions. (#b84a88b)
- Correction de problèmes d'accessibilité suite à un audit. (#6492ad1, #048765f)
- Ajout de tracking analytique sur le simulateur courant et le bouton "Modifier mes réponses". (#6e51291, #48caeec)
- Mise à jour des taux BNC Cipav avec Acre. (#ea8f00f)
- Mise à jour de la CSG non déductible sur les dividendes. (#c95c615)
- Utilisation de `SimpleField` et `SwitchContainer` dans la cessation d'activité. (#b8219e9)
- Remplacement du switch IR/IS par une question explicite dans la cessation d'activité. (#2683fb6)
- Précision que la rémunération inclut cotisations et contributions dans la cessation d'activité. (#34bb4f5)
- Exécution du lint:fix. (#eff2d30)
