## Changelog : aides-jeunes (30 derniers jours, au 26 août 2026)

### Résumé
Ce mois-ci, l'activité a été principalement concentrée sur la mise à jour et la fiabilisation des informations relatives aux aides. De nombreux dispositifs ont vu leurs conditions ou montants actualisés, et une campagne importante de correction de liens et de gestion de la confidentialité a été menée pour garantir la qualité de l'expérience utilisateur. Parallèlement, le moteur de calcul a bénéficié d'optimisations techniques pour gagner en précision et en stabilité.

### Évolutions fonctionnelles
- **Mise à jour des informations d'aides** : Actualisation des montants, des conditions d'éligibilité et des descriptions pour divers dispositifs (Permis de conduire/Pass'Permis [#5227, #5243, #5247], stages à l'étranger [#5226, #5246], aides régionales [#5257, #5248], BAFA/BAFD [#5236, #5190, #5189, #5188, #5187, #5185, #5186], et autres aides comme le Ticket Sport [#5240] ou la rémunération des stagiaires [#5245]).
- **Fiabilisation de l'accès aux informations** : Correction massive de liens rompus et passage de plusieurs dispositifs en mode "privé" pour assurer la cohérence des données (ex: Pass ZOU [#5249], Prêt d'études PER [#5216], Pass pass [#5215], et diverses bourses communales [#5217, #5218, #5219, #5220, #5194]).
- **Nouvelle fonctionnalité** : Mise en place d'un système d'identification spécifique pour les dispositifs de Paris Cité [#5160].

### Évolutions techniques
- **Optimisations du moteur Openfisca** : 
    - Amélioration du rendu des résultats pour les usagers déclarant un taux d'incapacité [#5212].
    - Précision du calcul des coûts réels sur les axes budgétaires [#5211].
    - Fiabilisation des chemins d'erreur et limitation de la durée des calculs [#5205].
- **Corrections de bugs** : Résolution d'un problème d'authentification par jeton lors d'appels échouant dans une iframe [#5210].
- **Maintenance et stabilité** : Gestion et résolution d'incidents de production liés aux mises à jour du moteur de calcul [#5204, #5207].

### Autres changements
- **Configuration** : Mise à jour de la liste des réviseurs dans le système d'assignation automatique [#5254].
