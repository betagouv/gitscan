## Changelog : dictaphone (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, dictaphone a connu une évolution significative, notamment avec l'ajout de fonctionnalités de corbeille (suppression et restauration de fichiers), une intégration améliorée de la transcription automatique via un service d'IA externe, et des améliorations majeures de l'interface utilisateur, en particulier pour la gestion des enregistrements et l'expérience mobile. L'application s'enrichit également d'une documentation intégrée.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de corbeille permettant de supprimer et restaurer des enregistrements. [#019b1c5](https://github.com/suitenumerique/dictaphone/commit/019b1c595961433f75741784964391900865890d)
- Intégration de la documentation directement dans l'application. [#5cf5b73](https://github.com/suitenumerique/dictaphone/commit/5cf5b731245f04b496468981317601785395316e)
- Affichage de la durée des enregistrements. [#4679bdd](https://github.com/suitenumerique/dictaphone/commit/4679bdd404296930f2481115731416719991f26a)
- Affichage des informations de suppression (badge "Supprimé") pour les enregistrements mis à la corbeille. [#6796e2a](https://github.com/suitenumerique/dictaphone/commit/6796e2a414a26710f73007949334756897405546)
- Amélioration de l'expérience utilisateur sur mobile avec une redirection spécifique. [#389857d](https://github.com/suitenumerique/dictaphone/commit/389857d4b416496464906765516698195669822c)
- Affichage du statut de transcription et du résumé dans l'interface utilisateur. [#145845e](https://github.com/suitenumerique/dictaphone/commit/145845e3135115473f14675f6471b90625f92681)
- Ajout d'un composant d'enregistrement audio. [#3920650](https://github.com/suitenumerique/dictaphone/commit/392065028a197664981611232627356f8175131a)
- Implémentation d'un modal d'upload audio. [#78ff857](https://github.com/suitenumerique/dictaphone/commit/78ff85756126f169656647163570b69f9a69148f)
- Prise en charge de la récupération de fichiers. [#b576bbf](https://github.com/suitenumerique/dictaphone/commit/b576bbf7369954966b948160b6999459a190176a)

### Évolutions techniques
- Intégration avec un service d'IA externe pour la transcription (alignement sur un nouveau contrat d'API). [#05a82af](https://github.com/suitenumerique/dictaphone/commit/05a82af9547696392587466498347312c7611f95) et [#bd777de](https://github.com/suitenumerique/dictaphone/commit/bd777de8384436154236261f7b489561d089835b)
- Correction de problèmes de permissions pour les jobs d'IA et les accès aux médias. [#8ff5071](https://github.com/suitenumerique/dictaphone/commit/8ff507161939540f63626665339a538b62f49f72)
- Amélioration de la gestion des erreurs lors de l'appel au service d'IA (création systématique d'un job et marquage comme échoué en cas d'erreur). [#0070201](https://github.com/suitenumerique/dictaphone/commit/00702013124393950681562a11d060f96145449e)
- Refactoring du format des clés des fichiers uploadés. [#cd5d67a](https://github.com/suitenumerique/dictaphone/commit/cd5d67a8951763848249f4968548b63177666635)
- Correction d'un problème de dépendance Dockerfile (libmagic manquante). [#342bc79](https://github.com/suitenumerique/dictaphone/commit/342bc79198f6772a80f3793289b816566a84299f)
- Publication d'une première version Helm. [#d240726](https://github.com/suitenumerique/dictaphone/commit/d2407264f8833b9517c9a46434f3868911444b1a) et [#13fc9dc](https://github.com/suitenumerique/dictaphone/commit/13fc9dc21082f885316199866336993711569787)

### Autres changements
- Amélioration du README pour une meilleure lisibilité. [#8e1c0a4](https://github.com/suitenumerique/dictaphone/commit/8e1c0a463b21b968f32374344b974c1969819d96)
- Corrections de labels de traduction. [#2c3ce06](https://github.com/suitenumerique/dictaphone/commit/2c3ce0692145391818678866336944495c652015)
- Amélioration de la réactivité de l'interface utilisateur. [#5bf0e13](https://github.com/suitenumerique/dictaphone/commit/5bf0e13931b4361a199559529627f7116599a56e) et [#af50a42](https://github.com/suitenumerique/dictaphone/commit/af50a4229a6456697761373166c4943247241924)
- Ajout d'un favicon. [#b620225](https://github.com/suitenumerique/dictaphone/commit/b6202258153847852969748536818214340f3613)
- Amélioration de l'interface utilisateur (couleurs, icônes, etc.). [#a6dbe78](https://github.com/suitenumerique/dictaphone/commit/a6dbe787f8f62666f7f7a174a935885b25992486) et [#ec9e6f2](https://github.com/suitenumerique/dictaphone/commit/ec9e6f2657848c7f156889a76961481263271575)
- Correction de la détection du besoin de rafraîchissement de l'API. [#d8cd6f8](https://github.com/suitenumerique/dictaphone/commit/d8cd6f899311792b16331914951d4b8701a89559)
- Support d'une réponse WhisperX plus souple. [#633a581](https://github.com/suitenumerique/dictaphone/commit/633a58106f4f38a2391544466330911975099846)
- Auto-rafraîchissement des jobs en attente toutes les 10 secondes. [#651a9c0](https://github.com/suitenumerique/dictaphone/commit/651a9c0f6a66439892396187818855461432946d)
- Amélioration du composant d'upload et du lecteur audio. [#f838275](https://github.com/suitenumerique/dictaphone/commit/f838275896944144f457983873071421a5699758)
- Nettoyage de la liste des enregistrements. [#64122be](https://github.com/suitenumerique/dictaphone/commit/64122be14227a94631155113917c55a453919c45)
- Amélioration du panel de gauche. [#8139b9b](https://github.com/suitenumerique/dictaphone/commit/8139b9b315357693976628959f27964984b1918d) et [#c49f155](https://github.com/suitenumerique/dictaphone/commit/c49f15573164029b76350a16f72f142467634466)
- Amélioration de l'UI-kit. [#86dcb95](https://github.com/suitenumerique/dictaphone/commit/86dcb95422922516796789888686336623133697)
- Amélioration de l'expérience de glisser-déposer. [#7d1be5d](https://github.com/suitenumerique/dictaphone/commit/7d1be5d76364749419115636211316264f2f7d1c)
