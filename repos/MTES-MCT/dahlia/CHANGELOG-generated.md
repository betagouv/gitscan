## Changelog : dahlia (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, dahlia a bénéficié d'importantes améliorations axées sur la fiabilité, la sécurité et la fluidité de l'expérience utilisateur. Les évolutions majeures incluent un renforcement de la traçabilité des actions, une meilleure isolation des données entre les juridictions et une optimisation des processus de synchronisation des dossiers.

### Évolutions fonctionnelles
- **Interface et navigation** : Renommage de certains éléments pour plus de clarté (Tags vers Mots clés, etc.) [#146], ajout d'un bouton d'accès au formulaire de retour utilisateur [#180], mise à disposition des pages légales pour tous les utilisateurs [#155], et restriction de l'onglet debug aux seuls administrateurs [#186].
- **Gestion métier** : Identification des décisions de la COMED [#156], synchronisation complète des dossiers pour le département 69 [#159], ajout du champ statut lors de l'export de la classification [#153], et application de nouvelles règles de classification [#170].
- **Expérience utilisateur** : Amélioration du processus de déconnexion avec redirection vers ProConnect [#169] et correction de l'affichage des messages d'erreur pour plus de clarté [#173].

### Évolutions techniques
- **Sécurité et traçabilité** : Mise en place de logs d'audit pour les refus d'accès [#174] et les actions administratives [#158], renforcement de la vérification de la validité des sessions [#171], et masquage des détails techniques sensibles (erreurs Prisma, Télérecours) en environnement de production [#157, #154].
- **Performance et fiabilité** : Passage de la synchronisation des dossiers en mode asynchrone [#152], ajout d'un limiteur de débit (rate limit) sur les appels à l'API Télérecours [#187], et mise en place d'une tâche planifiée (cron) pour le département 93 [#188].
- **Architecture et données** : Intégration du code de juridiction dans les clés primaires pour une meilleure isolation des données [#175], gestion de l'isolation des instances pour certains dossiers [#160], et garantie de l'étanchéité des données entre juridictions lors des suppressions [#161].
- **Maintenance** : Mises à jour de sécurité et du framework Next.js [#184, #167, #166].
